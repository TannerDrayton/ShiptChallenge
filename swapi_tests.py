import requests
import json

def jprint(obj):
  #This is used as a viewing tool, it formats data recieved from API
  text = json.dumps(obj,sort_keys=True,indent=4)
  print(text)

def obi():
  init_request = requests.get('https://swapi.co/api/people?search=Obi')
  #jprint(init_request.json())
  init_response = init_request.json()
  second_request = requests.get(init_response['results'][0]['films'][5])
  #jprint(second_request.json())
  second_response = second_request.json()
  return second_response['title']

#obi()

def test_obi():
  assert obi() == 'A New Hope'

def enterprise():
  init_request = requests.get('https://swapi.co/api/starships?search=enterprise')
  init_response = init_request.json()
  return init_response['count']
  
def test_enterprise():
  assert enterprise() == 0

def chewie():
  init_request = requests.get('https://swapi.co/api/people?search=Chewbacca')
  init_response = init_request.json()
  second_request = requests.get(init_response['results'][0]['species'][0])
  second_response = second_request.json()
  return second_response['name']

def test_chewie():
  assert chewie() == 'Wookiee'

def starships():
  fit_to_fly = False
  init_request = requests.get('https://swapi.co/api/starships/')
  init_response = init_request.json()
  #jprint(init_response.json())
  results_key = (init_response['results'][0])
  if 'name' in results_key:
    has_name = True
  else:
    has_name = False
  if 'model' in results_key:
    has_model = True
  else:
    has_model = False
  if 'crew' in results_key:
    has_crew = True
  else: 
    has_crew = False
  if 'hyperdrive_rating' in results_key:
    has_hyperdrive = True
  else: 
    has_hyperdrive = False
  if 'pilots' in results_key:
    has_pilots = True
  else:
    has_pilots = False
  if has_name == True and has_model == True and has_crew == True and has_hyperdrive == True and has_pilots == True:
    fit_to_fly = True
  return fit_to_fly

def test_starships():
  assert starships() == True
