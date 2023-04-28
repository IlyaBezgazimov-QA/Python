import requests

token = '14ba374961eecd1dd3152f1c5d738835'
base_url = 'https://pokemonbattle.me:9104/'


'''response_add_pockemon = requests.post (f'{base_url}pokemons', headers={'trainer_token' : token }, json= {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})

print(response_add_pockemon.text)'''


response_change_pockemon = requests.put (f'{base_url}pokemons', headers={'trainer_token' : token }, json= {
    "pokemon_id": "9182",
    "name": "001",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})

print(response_change_pockemon.text)

response_catch_in_pokeball = requests.post (f'{base_url}trainers/add_pokeball', headers={'trainer_token' : token }, json= {
    "pokemon_id": "9182"
})
print(response_catch_in_pokeball.text)
