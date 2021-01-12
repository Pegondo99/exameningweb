from django.urls import path
from servidor import views

urlpatterns = [
    path('libros/', views.LibroList.as_view()),
    path('libros/<str:id>', views.LibroDetails.as_view()),
    path('autores/', views.AutorList.as_view()),
    path('autores/<str:id>', views.AutorDetails.as_view()),
]
