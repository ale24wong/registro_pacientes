from django.db import models
from django.utils import timezone

# Create your models here.
class Paciente(models.Model):
	nombres = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	telefono = models.CharField(max_length=100)
	date_added = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return '{} {}'.format(self.nombres, self.apellidos)