import cloudinary
from django.shortcuts import render, redirect

from cliente.services.autores_services import get_all_autores, insert_autor
from cliente.services.libros_services import get_all_libros


def ver_libros(request):
    libros = get_all_libros()
    autores = get_all_autores()

    for libro in libros:
        autor = [a for a in autores if a['id'] == libro['autor']]
        if autor and autor[0]:
            autor = autor[0]
            libro['autor'] = {"id": libro['autor'], "nombre": autor['nombre']}

    return render(request, "ver_libros.html", {"libros": libros})


def ver_autores(request):
    autores = get_all_autores()

    return render(request, "autores.html", {"autores": autores})


def anadir_autor(request):
    autor = {"nombre": request.POST["nombre"]}

    foto_url = ""
    if len(request.FILES) > 0:
        file = request.FILES["foto"]
        result = cloudinary.uploader.upload(file, transformation=[
            {'width': 350, 'height': 350, 'crop': 'thumb', }])
        foto_url = result["url"]

    autor["foto"] = foto_url

    insert_autor(autor)

    return redirect("/cliente/autores/")
