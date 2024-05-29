from rest_framework import generics
from .models import Empleado
from .serializers import EmpleadoSerializer

class EmpleadoList(generics.ListCreateAPIView):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()
        
    
class EmpleadoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()

