#REST
from rest_framework import generics
from .models import Empleado, Departamento
from .serializers import EmpleadoSerializer, DepartamentoSerializer
#CRUD NORMAL
from django.shortcuts import render, redirect
from api.forms import EmpleadoForm, DepartamentoForm
from api.models import Empleado, Departamento
#login
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import LoginForm
#Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

#REST FW
class EmpleadoList(generics.ListCreateAPIView):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()
        
    
class EmpleadoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()

class DepartamentoList(generics.ListCreateAPIView):
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all()
        
    
class DepartamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all()

#CRUD NORMAL
def emp(request):
    form = EmpleadoForm()
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('/api/show')
    
        
    return render(request,'index.html',{'form':form})

def show(request):
    empleados = Empleado.objects.all()
    return render(request,"show.html",{'empleados':empleados})

def edit(request, id):
    empleado = Empleado.objects.get(id=id)
    return render(request,'edit.html', {'empleado':empleado})

def update(request, id):
    empleado = Empleado.objects.get(id=id)
    form = EmpleadoForm(request.POST, instance = empleado)
    if form.is_valid():
        form.save()
        return redirect("/api/show")
    return render(request, 'edit.html', {'empleado': empleado})

def delete(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect("/api/show")

#LOGIN
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)

#Token
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'message': 'usuario validado correctamente',
            'token': token.key,
            'username': user.username,
            'status': status.HTTP_200_OK 
        })