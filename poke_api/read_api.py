import requests
import json
from flask import jsonify

class GetApi:
    def __init__(self):
        self.endpoint = None

    def get_response(self, pokename):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokename}/")
        response_json = json.loads(response.text)
        types = response_json['types']
        pokemon_types = []
        for x in types:
            pokemon_types.append(x['type']['name'])
        pokemon_types = str(pokemon_types[0])
        pokemon_name = response_json['name']
        pokemon_id = response_json['id']
        pokemon_height = str(response_json['height'])
        pokemon_weight = str(response_json['weight'])
        

        return {
            'pokemon_name': pokemon_name,
            'pokemon_id': pokemon_id,
            'pokemon_types': pokemon_types,
            'pokemon_height': pokemon_height,
            'pokemon_weight': pokemon_weight
        }