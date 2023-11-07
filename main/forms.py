from django import forms
from .models import Specialization, Developer, State

class ProjectForm(forms.Form):
    id = forms.CharField(label="Nazwa Projektu", max_length=100)
    user_name = forms.CharField(label="Nazwa Użytkownika", max_length=100)
    developers = forms.ModelMultipleChoiceField(queryset=Developer.objects.all(), label='Dodaj deweloperów', widget=forms.CheckboxSelectMultiple)

class DeveloperForm(forms.Form):
    id = forms.CharField(label='Nick', max_length=300)
    name = forms.CharField(label='Name', max_length=300)
    specialization = forms.ChoiceField(
        label='Specjalizacja', 
        choices=Specialization.choices,
        )

class TaskForm(forms.Form):
    name = forms.CharField(label="Podaj Taska",max_length=200)
    credentials = forms.ChoiceField(
        label='Specjalizacja', 
        choices=Specialization.choices,
        )
    state = forms.ChoiceField(
        label='Stan taska', 
        choices=State.choices,
        )
    developers = forms.ModelMultipleChoiceField(queryset=Developer.objects.all(), 
                                                label='Dodaj deweloperów(opcjonalnie)',
                                                  widget=forms.CheckboxSelectMultiple,
                                                  required=False)
   
    estimation = forms.IntegerField(label="Podaj estymację(liczbę fibonacciego)")
    created_by = forms.CharField(label="Nazwa użytkownika")