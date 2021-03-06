from cliente.services.services import generate_request, response_2_dict


def get_all_libros():
    # Llamo a la API.
    url = "https://exameningweb.herokuapp.com/libros/"
    params = {}
    response = generate_request(url, params)
    if response:
        return response_2_dict(response)