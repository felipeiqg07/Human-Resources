from django.urls import path
from .views import EmpleadoList, EmpleadoDetail

urlpatterns = [
    path('empleado/', EmpleadoList.as_view()),
    path('empleado/<int:pk>/', EmpleadoDetail.as_view()),


]