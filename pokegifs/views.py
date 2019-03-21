from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import json
import requests
import os

from random import choice

def show_pokemon(request, pokemon_id):
    # querythe Pokemon API
    pokemon_url = f"http://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    json_response_1 = requests.get(pokemon_url)
    body_1 = json.loads(json_response_1.content)
    id = body_1["id"]
    name = body_1["name"]
    types = body_1["types"]
    # retrieve all the type names from types
    type_names = []
    for type in types:
        t = type["type"]
        type_name = t["name"]
        type_names.append(type_name)
    # query the GIPHY API
    giphy_key = os.environ.get("GIPHY_KEY")
    giphy_url = f"https://api.giphy.com/v1/gifs/search?api_key={giphy_key}&q={name}&rating=g"
    json_response_2 = requests.get(giphy_url)
    body_2 = json.loads(json_response_2.content)
    all_gifs = body_2["data"]
    random_gif = choice(all_gifs)
    gif_url = random_gif["url"]
    # return a JSON response
    return JsonResponse({
        "id": id,
        "name": name,
        "types": type_names,
        "gif": gif_url
    })
