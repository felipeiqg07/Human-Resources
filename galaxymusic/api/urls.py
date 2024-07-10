from django.urls import path
from api import views
from .views import EmpleadoList, EmpleadoDetail, DepartamentoList, DepartamentoDetail, CustomLoginView, CustomAuthToken
#Token
from rest_framework.authtoken import views as authviews

urlpatterns = [
    #REST
    path('empleado/', EmpleadoList.as_view()),
    path('empleado/<int:pk>/', EmpleadoDetail.as_view()),
    path('departamento/', DepartamentoList.as_view()),
    path('departamento/<int:pk>/', DepartamentoDetail.as_view()),
    #CRUD
    path('emp/',views.emp),
    path('show/',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    #LOGIN
    path('login/', CustomLoginView.as_view()),
    #Token
    #path('api-token-auth/', authviews.obtain_auth_token),
    path('api-token-auth/', CustomAuthToken.as_view())


]