# acceso/serializers.py
from rest_framework import serializers
from .models import (
    Vivienda, Residente, Vehiculo,
    Visitante, Guardia, Invitacion, RegistroAcceso
)


# -------------------------
#  VIVIENDA
# -------------------------
class ViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vivienda
        fields = ("id", "numero", "calle", "propietario", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")


# -------------------------
#  RESIDENTE
# -------------------------
class ResidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residente
        fields = ("id", "nombre", "cedula", "telefono", "vivienda",
                  "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")


# -------------------------
#  VEHICULO
# -------------------------
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ("id", "placa", "marca", "modelo", "residente",
                  "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")


# -------------------------
#  VISITANTE
# -------------------------
class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = ("id", "nombre", "cedula", "telefono",
                  "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")


# -------------------------
#  GUARDIA
# -------------------------
class GuardiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardia
        fields = ("id", "nombre", "usuario", "clave",
                  "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")


# -------------------------
#  INVITACION
# -------------------------
class InvitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitacion
        fields = ("id", "residente", "visitante", "fecha", "codigo",
                  "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")


# -------------------------
#  REGISTRO ACCESO
# -------------------------
class RegistroAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAcceso
        fields = (
            "id", "visitante", "vehiculo", "guardia",
            "invitacion", "tipo", "fecha_hora"
        )
        read_only_fields = ("id", "fecha_hora")
