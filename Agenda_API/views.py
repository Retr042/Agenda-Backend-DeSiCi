from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets, filters
from .serializers import ContactoSerializer
from .models import Contacto, Direccion, Telefono


class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all().order_by('id')
    serializer_class = ContactoSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'telefonos__numero']