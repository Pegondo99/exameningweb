import json
import requests
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

headers = {'content_type': 'application/json'}


def generate_request(url, params={}):
    response = requests.get(url, params=params)
    if response.status_code >= 200 and response.status_code < 300:
        return response.json()


def response_2_dict(response):
    # No hago get de nada de la response porque lo quiero todo
    json_response = json.dumps(response)
    result = json.loads(json_response)  # String to list
    return result


def generate_post(url, datos):
    print(datos)
    response = requests.post(url, json=datos, headers=headers)
    print(response.__dict__)
    print(response.status_code)
    print("Vamos a hacer un POST a: " + url)
    return response


def generate_delete(url):
    response = requests.delete(url)
    print("Vamos a hacer un DELETE a: " + url)
    return response


def generate_put(url, datos):
    response = requests.put(url, json=datos, headers=headers)
    print(response.__dict__)
    print(response.status_code)
    print("Vamos a hacer un PUT a: " + url)
    return response