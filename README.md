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
# short script to test put requests
import requests
import json

project = "DataLine" # name of the project
task = 2 # number id of edited task
new_status = "TO_DO" # fill with "TO_DO", "IN_PROGRESS" or "COMPLETED"
url = "http://127.0.0.1:8000/project/DataLine/task/2"
data = {'new_status': 'COMPLETED'}

headers = {'Content-Type': 'application/json'}
response = requests.put(url, data=json.dumps(data), headers=headers)

print("Status code:", response.status_code)
print("Response content:", response.text)'''
