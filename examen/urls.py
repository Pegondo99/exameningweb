from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('servidor.urls')), #Redirijo las URL a servidor.urls
    path('cliente/', include('cliente.urls')), #Redirijo las URL a cliente.urls
]