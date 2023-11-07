## TaskManager - Proste narzędzie do zarządzania projektami

### Domena - Pod tą domeną znajduje się działające narzędzie
https://taskmanager-hubi-99039daa47b1.herokuapp.com/

### Implementacja algorytmu

Algorytm znajduje się w pliku `taskmanager/main/views.py`. 
def algorithm(...)

### Technologie wykorzystane w projekcie

- Framework: Django
- Baza danych: PostgreSQL
- Hosting: Heroku

### Interfejsy
Interfejsy znajdują się w pliku `taskmanager/main/models.py`. 

### Update taska żądaniem PUT
Task można zupdatować za pomocą żądania POST z użyciem forms.
Jeśli chcemy użyć żądania PUT polecam użyć kodu:
## TaskManager - Proste narzędzie do zarządzania projektami

### Domena - Pod tą domeną znajduje się działające narzędzie
https://taskmanager-hubi-99039daa47b1.herokuapp.com/

### Implementacja algorytmu

Algorytm znajduje się w pliku `taskmanager/main/views.py`. 
def algorithm(...)

### Technologie wykorzystane w projekcie

- Framework: Django
- Baza danych: PostgreSQL
- Hosting: Heroku

### Interfejsy
Interfejsy znajdują się w pliku `taskmanager/main/models.py`. 

### Update taska żądaniem PUT
Task można zupdatować za pomocą żądania POST z użyciem forms.
Jeśli chcemy użyć żądania PUT polecam użyć kodu:

'''
import requests
import json

project = "DataLine"
task = 2 # number id of edited task
new_status = "TO_DO" # fill with "TO_DO", "IN_PROGRESS" or "COMPLETED"
url = "https://taskmanager-hubi-99039daa47b1.herokuapp.com/project/{nazwa_projektu}/task/{int_id_task}"
data = {'new_status': 'COMPLETED'}

headers = {'Content-Type': 'application/json'}
response = requests.put(url, data=json.dumps(data), headers=headers)

print("Status code:", response.status_code)
print("Response content:", response.text)'''
