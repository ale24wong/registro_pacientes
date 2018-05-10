from django.shortcuts import render, redirect
from . import models
from . import forms

# Create your views here.

#Mostrar lista de pacientes
def index(request):
	pacientes = models.Paciente.objects.order_by('-date_added')

	context = {'pacientes' : pacientes}

	return render(request, 'index.html', context)

#Crear nuevo paciente
def crear_paciente(request):
	if request.method == 'POST':
		form = forms.PacienteForm(request.POST or None)

		if form.is_valid():
			crear_paciente= models.Paciente(
				nombres=request.POST['nombres'],
				apellidos = request.POST['apellidos'],
				telefono = request.POST['telefono']
				)
			crear_paciente.save()
			return redirect('index')
	else:
		form = forms.PacienteForm()

	context = {'form' : form}
	return render(request, 'formulario_paciente.html', context)

#Borrar paciente
def borrar_paciente(request, id):
	paciente = models.Paciente.objects.get(id=id)  

	if request.method=='POST':
		paciente.delete()
		return redirect('index')

	context = {'paciente' : paciente}
	return render(request, 'borrar_paciente.html', context)