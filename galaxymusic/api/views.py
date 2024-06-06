from rest_framework import generics
from .models import Empleado, Departamento
from .serializers import EmpleadoSerializer, DepartamentoSerializer

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

