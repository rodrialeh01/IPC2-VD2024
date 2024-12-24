from django.urls import path

from . import views

urlpatterns = [
    #path='' == http://localhost:8000/
    #path='hola/' == http://localhost:8000/hola/
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('signin/', views.iniciarSesion, name='signin'),
    path('admin/', views.adminPage, name='admin'),
    path('user/', views.userPage, name='user'),
    path('admin/carga/', views.cargaAdminPage, name='carga'),
    path('admin/cargaxml/', views.cargarXML, name='cargaxml'),
    path('admin/cargausers/', views.enviarUsersXML, name='cargausers'),
    path('admin/users/', views.verUsuariosPage, name='users'),
    path('admin/usersxml/', views.verUsuariosXMLPage, name='usersxml'),
    path('admin/ayuda/', views.ayuda, name='ayuda'),
    path('logout/', views.cerrarSesion, name='logout'),
]