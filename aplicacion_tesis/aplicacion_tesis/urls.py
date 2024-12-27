"""aplicacion_tesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('',views.index, name='index'),
    path('admin/', admin.site.urls),
    path('register/', views.register,name='register'),
    path('user_login/',views.user_login,name="user_login"),
    path('logout/',views.user_logout,name ="user_logout"),
    path('diagnosticar/',views.diagnosticar,name ="diagnosis_view"),
    path('diagnostico/', views.predecir, name='predecir'),
    path('reentrenar_modelo/', views.reentrenar_modelo, name='reentrenar'),
    path('reentrenar/', views.reentrenar, name='reentreno'),
    path('recuperar_contrasena/', views.solicitud_cambiar_contrasena, name='recuperar_contrasena'),
    path('cambiar_contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),
    path('integrar_diagnostico_medico/', views.integrar_diagnostico_medico, name='integrar_diagnostico'),
]