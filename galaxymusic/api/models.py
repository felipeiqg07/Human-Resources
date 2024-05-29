from django.db import models
 
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_p = models.CharField(max_length=100)
    apellido_m = models.CharField(max_length=100)
    fec_nac = models.DateField()
    salario = models.IntegerField()
    fec_contra = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.nombre