from django.shortcuts import render
from .models import Paciente

# Create your views here.

def listar_paciente(request):    
    return render(request, 'listar_pacientes.html', {'lista_pacientes': Paciente.objects.all()})