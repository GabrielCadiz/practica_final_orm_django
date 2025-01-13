from django.db import models

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'laboratorio_tabla'

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE, related_name='director')
    especialidad = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'director_tabla'

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(
        Laboratorio, on_delete=models.CASCADE, related_name='productos'
    )
    f_fabricacion = models.IntegerField()
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'producto_tabla'
