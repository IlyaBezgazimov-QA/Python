import requests
import pytest


def test_stetus_code_and_part_of_body ():
    token = '14ba374961eecd1dd3152f1c5d738835'
    response = requests.get ('https://pokemonbattle.me:9104/trainers', params={'trainer_id' : 3989})
    
    assert response.status_code == 200
    assert response.json()['trainer_name'] == 'il'

