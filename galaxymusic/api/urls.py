from django.urls import path
from .views import EmpleadoList, EmpleadoDetail, DepartamentoList, DepartamentoDetail

urlpatterns = [
    path('empleado/', EmpleadoList.as_view()),
    path('empleado/<int:pk>/', EmpleadoDetail.as_view()),
    path('departamento/', DepartamentoList.as_view()),
    path('departamento/<int:pk>/', DepartamentoDetail.as_view()),

]