import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '40ed81bd756a1104b8d15ca9c71249e3'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_pokemons = {
    "pokemon_id": "136361"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
 print(response.text)'''

'''response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response.text)'''

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemons)
print(response.text)
