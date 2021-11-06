from django.db import models

# Create your models here.
class Producto (models.Model):

    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    cantidad = models.PositiveIntegerField()
    precio = models.FloatField()
    def __str__(self):
        return self.nombre
