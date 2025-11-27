# acceso/views.py
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .permissions import BasicRolePermission

from .models import (
    Vivienda, Residente, Vehiculo,
    Visitante, Guardia, Invitacion, RegistroAcceso
)
from .serializers import (
    ViviendaSerializer, ResidenteSerializer, VehiculoSerializer,
    VisitanteSerializer, GuardiaSerializer, InvitacionSerializer,
    RegistroAccesoSerializer
)


@api_view(["GET"])
def api_home(request):
    base = request.build_absolute_uri('/api/').rstrip('/')
    return Response({
        "viviendas": f"{base}/viviendas/",
        "residentes": f"{base}/residentes/",
        "vehiculos": f"{base}/vehiculos/",
        "visitantes": f"{base}/visitantes/",
        "guardias": f"{base}/guardias/",
        "invitaciones": f"{base}/invitaciones/",
        "registros": f"{base}/registros/"
    })


class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer

class ResidenteViewSet(viewsets.ModelViewSet):
    queryset = Residente.objects.all()
    serializer_class = ResidenteSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer

class GuardiaViewSet(viewsets.ModelViewSet):
    queryset = Guardia.objects.all()
    serializer_class = GuardiaSerializer

class InvitacionViewSet(viewsets.ModelViewSet):
    queryset = Invitacion.objects.all()
    serializer_class = InvitacionSerializer

class RegistroAccesoViewSet(viewsets.ModelViewSet):
    queryset = RegistroAcceso.objects.all()
    serializer_class = RegistroAccesoSerializer
