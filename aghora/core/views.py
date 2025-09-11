from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import requests
import json
import hashlib

def index(request):
    api_prefix = settings.API_URL  # URL de base de l’API
    api_key = settings.API_KEY  # Ton API key
    secret_key = settings.API_SECRET # Ton secret key
    endpoint = "decode"
    vin = "wf0mxxgbwm8r43240".upper()

    # Calcul du controlSum (SHA1 puis on prend les 10 premiers caractères)
    raw_string = f"{vin}|{endpoint}|{api_key}|{secret_key}"
    control_sum = hashlib.sha1(raw_string.encode("utf-8")).hexdigest()[:10]

    # Construire l’URL
    url = f"{api_prefix}/{api_key}/{control_sum}/{endpoint}/{vin}.json"
    response = requests.get(url)
    data = response.json()
    print(json.dumps(data, indent=4))  # Afficher la réponse formatée

    return render(request,'index.html')

