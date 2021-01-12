from rest_framework_mongoengine import generics
from servidor.models import Libro, Autor
from servidor.serializers import LibroSerializer, AutorSerializer


class LibroList(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    # Filtros
    def filter_queryset(self, queryset):
        #Los libros con editorial `editorial`
        editorial = self.request.query_params.get('editorial', None)
        if editorial:
            queryset = queryset.filter(detalles__editorial__icontains=editorial)

        return queryset


class LibroDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class AutorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
