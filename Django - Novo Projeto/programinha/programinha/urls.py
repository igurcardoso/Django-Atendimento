from django.contrib import admin
from django.urls import path
from aplicacao_programinha.views import listar_paciente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar_paciente/', listar_paciente)
]
