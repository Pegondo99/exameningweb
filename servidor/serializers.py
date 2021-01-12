from rest_framework_mongoengine import serializers
from servidor.models import Libro, Autor


class LibroSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class AutorSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Autor
        fields = '__all__'