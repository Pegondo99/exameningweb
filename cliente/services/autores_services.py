from cliente.services.services import generate_request, response_2_dict, generate_post

base_url = "https://exameningweb.herokuapp.com/autores/"


def get_all_autores():
    # Llamo a la API.
    params = {}
    response = generate_request(base_url, params)
    if response:
        return response_2_dict(response)


def insert_autor(autor):
    response = generate_post(base_url, autor)
    return response
