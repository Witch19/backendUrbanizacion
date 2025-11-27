# acceso/models.py
from django.db import models


# -------------------------
#  VIVIENDA
# -------------------------
class Vivienda(models.Model):
    numero = models.CharField(max_length=10)
    calle = models.CharField(max_length=80)
    propietario = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("numero",)

    def __str__(self):
        return f"Casa {self.numero} - {self.calle}"


# -------------------------
#  RESIDENTE
# -------------------------
class Residente(models.Model):
    nombre = models.CharField(max_length=120)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)

    vivienda = models.ForeignKey(
        Vivienda,
        on_delete=models.CASCADE,
        related_name="residentes"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return self.nombre


# -------------------------
#  VEHICULO
# -------------------------
class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

    residente = models.ForeignKey(
        Residente,
        on_delete=models.CASCADE,
        related_name="vehiculos"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("placa",)

    def __str__(self):
        return self.placa


# -------------------------
#  VISITANTE
# -------------------------
class Visitante(models.Model):
    nombre = models.CharField(max_length=120)
    cedula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return self.nombre


# -------------------------
#  GUARDIA
# -------------------------
class Guardia(models.Model):
    nombre = models.CharField(max_length=120)
    usuario = models.CharField(max_length=30, unique=True)
    clave = models.CharField(max_length=200)   # Se recomienda almacenar HASH

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return self.nombre


# -------------------------
#  INVITACION / AUTORIZACIÓN
# -------------------------
class Invitacion(models.Model):
    residente = models.ForeignKey(
        Residente,
        on_delete=models.CASCADE,
        related_name="invitaciones"
    )

    visitante = models.ForeignKey(
        Visitante,
        on_delete=models.CASCADE
    )

    fecha = models.DateField()
    codigo = models.CharField(max_length=10, unique=True)   # Código QR, PIN, etc.

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("fecha",)

    def __str__(self):
        return f"Invitación {self.codigo}"


# -------------------------
#  REGISTRO DE ACCESO
# -------------------------
class RegistroAcceso(models.Model):
    TIPO_MOVIMIENTO = (
        ("ENTRADA", "Entrada"),
        ("SALIDA", "Salida"),
    )

    visitante = models.ForeignKey(
        Visitante,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    guardia = models.ForeignKey(
        Guardia,
        on_delete=models.SET_NULL,
        null=True
    )

    invitacion = models.ForeignKey(
        Invitacion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    tipo = models.CharField(max_length=20, choices=TIPO_MOVIMIENTO)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-fecha_hora",)

    def __str__(self):
        return f"{self.tipo} - {self.fecha_hora}"
