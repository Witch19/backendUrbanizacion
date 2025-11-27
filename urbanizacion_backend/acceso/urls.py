# acceso/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    ViviendaViewSet, ResidenteViewSet, VehiculoViewSet,
    VisitanteViewSet, GuardiaViewSet, InvitacionViewSet,
    RegistroAccesoViewSet, api_home
)

router = DefaultRouter()
router.register(r'viviendas', ViviendaViewSet, basename='vivienda')
router.register(r'residentes', ResidenteViewSet, basename='residente')
router.register(r'vehiculos', VehiculoViewSet, basename='vehiculo')
router.register(r'visitantes', VisitanteViewSet, basename='visitante')
router.register(r'guardias', GuardiaViewSet, basename='guardia')
router.register(r'invitaciones', InvitacionViewSet, basename='invitacion')
router.register(r'registros', RegistroAccesoViewSet, basename='registro')

urlpatterns = router.urls + [
    path('', api_home, name='api-acceso-home'),
]
