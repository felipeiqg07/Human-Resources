from django import forms
from api.models import Empleado, Departamento
from django.contrib.auth.forms import AuthenticationForm

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre','apellido_p','apellido_m','salario','correo','usuario','contrasena']
        

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('__all__')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario o Email', max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
   