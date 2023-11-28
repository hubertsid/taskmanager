from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Developer, Project, Task, State
from .forms import ProjectForm, DeveloperForm, TaskForm
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Funkcje pomocnicze
def is_project(id):
    return Project.objects.filter(id=id).exists()


def repetition_check(form, tag):
    id = form.cleaned_data['id']
    if tag == 'users':
        return not Project.objects.filter(id=id).exists()
    elif tag == 'projects':
        return not Developer.objects.filter(id=id).exists()

    return False


def is_fibonacci(number):
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
    return a == number


def algorithm(estimation, completed, assignments):
    #Algorithm is counting points
    #Developer with lowest score, gets the job
    points = 0

    #score 1
    #Comparing task estimation with completed tasks
    #we have to find closest number
    closest = 100_000_000
    for i in completed:
        dist = abs(estimation-i.estimation)
        if dist < closest:
            closest = dist 
    points += closest

    #score 2
    #checking if dev got assignments
    #if it did score goes up tenfold
    points += assignments*10

    return points


# Widoki
def index(request):
    proj = Project.objects.all()
    task = Task.objects.all()
    devs = Developer.objects.all()
    return render(request, "index.html", {'proj': proj, 'task': task, 'devs': devs})


def users(request):
    if request.method == "POST":
        form = DeveloperForm(request.POST)
        if form.is_valid() and repetition_check(form, 'users'):

            new_developer = Developer(
                id=form.cleaned_data['id'],
                name=form.cleaned_data['name'],
                specialization=form.cleaned_data['specialization']
            )

            new_developer.save()
            return HttpResponseRedirect('/users/')
        else:
            return HttpResponse("Obiekt o tej nazwie znajduje się już w bazie danych")
    else:
        form = DeveloperForm()

    return render(request, "users.html", {'form': form})


def project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid() and repetition_check(form, 'projects'):
            new_project = Project(
                id=form.cleaned_data['id'],
                user=form.cleaned_data['user_name'],
            )

            # Podatność SQL Injection
            new_project.save()
            for i in form.cleaned_data['developers']:
                dev = Developer.objects.get(id=i)
                new_project.developers.add(dev)
            new_project.save()

            return HttpResponseRedirect("/project/")
        else:
            return HttpResponse("Obiekt o tej nazwie znajduje się już w bazie danych")

    else:
        form = ProjectForm()
    return render(request, "projects.html", {'form': form})

def assignment(request,id):
    #devs assignment algorithm

    # step 1 - find tasks with state TO_DO in this project
    task = Task.objects.filter(project_id=id,state="TO_DO")
    obj = {}
    for t in task:
        # step 2 - find specialization of task
        spec = t.credentials
        # step 3 - find a dev with this specialization
        devs = Developer.objects.filter(specialization=f"{spec}")

        low_score = 100_000_000
        best_dev = None
        assigned_devs = []
        for dev in devs:
            # step 4 - find completed tasks by that dev
            comp = Task.objects.filter(state="COMPLETED",developers=dev)

            # step 5 - simple algorithm -> compare historical tasks completed by dev with estimation of search task
            score = algorithm(t.estimation,comp,assigned_devs.count(dev.id))
            if score <= low_score:
                best_dev = dev
                low_score = score
        if best_dev != None:
            assigned_devs.append(best_dev.id)
            obj[t] = best_dev

    return render(request,"assignments.html",{'obj':obj,'id':id})
  

def project_info(request, id):
    if is_project(id):
        obj = Project.objects.get(id=id)
        return render(request, "projectinfo.html", {"obj": obj})
    else:
        dev = Developer.objects.get(id=id)
        proj = list(Project.objects.filter(developers__id=id))
        return render(request, "userinfo.html", {"dev": dev, "proj": proj})


def tasks(request, id=None):
    obj = Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            if not is_fibonacci(form.cleaned_data['estimation']):
                return HttpResponse("Liczba nie jest liczbą Fibonacciego")

            task = Task(
                name=form.cleaned_data['name'],
                project_id=id,
                credentials=form.cleaned_data['credentials'],
                state=form.cleaned_data['state'],
                estimation=form.cleaned_data['estimation'],
                created_at=datetime.datetime.now(),
                created_by=form.cleaned_data['created_by']
            )
            task.save()

            proj = Project.objects.get(id=id)
            proj.tasks.add(task)
            proj.save()
            for i in form.cleaned_data['developers']:
                dev = Developer.objects.get(id=i)
                proj.developers.add(dev)
                task.developers.add(dev)
            task.save()
            proj.save()
            return HttpResponse("Task dodany")
    elif id != None:
        proj = Project.objects.get(id=id)
        form = TaskForm()
        form.developers = proj.developers.all()
    else:
        form = TaskForm()
    return render(request, "task.html", {'id': id, 'form': form, 'obj': obj})
    
def assignment_add_dev(request, id, assignment_id):
    if request.method=="POST":
        task = Task.objects.get(id=assignment_id)
        cust_id = request.POST.get('custId')
        task.developers.add(cust_id)
        task.save()
        return HttpResponse("Developer dodany do taska")

@csrf_exempt # decorator for csrf exception
def edit_task_status(request, id, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'PUT':
        try:
            # Pobierz nowy status z żądania
            data = json.loads(request.body)
            new_status = data.get('new_status')
            task.state = new_status
            task.save()
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Niepoprawny format JSON'}, status=400)
        
        return JsonResponse({'message': 'Task status updated successfully.'})
    elif request.method == "POST":
        new_state = request.POST.get('task_state')
        task.state = new_state
        task.save()
        return HttpResponse("Status zmieniono")

    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)