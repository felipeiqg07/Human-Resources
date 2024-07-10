from django.db import models
 
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_p = models.CharField(max_length=100)
    apellido_m = models.CharField(max_length=100)
    salario = models.IntegerField()
    fec_contra = models.DateField(auto_now_add=True)
    correo = models.EmailField(max_length=100, default='no asignado')
    usuario = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=20)


    def __str__(self):
        return self.nombre
    

class Departamento(models.Model):
    nom_depa = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre