from django.urls import path
from cliente import views

urlpatterns = [
    path('libros/', views.ver_libros),
    path('autores/', views.ver_autores),
    path('anadir_autor/', views.anadir_autor),
]
