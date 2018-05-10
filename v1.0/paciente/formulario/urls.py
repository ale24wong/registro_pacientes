from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('crear_paciente', views.crear_paciente, name='crear_paciente'),
	path('borrar_paciente/<int:id>/', views.borrar_paciente, name='borrar_paciente'),
]