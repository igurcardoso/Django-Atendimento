from django.contrib import admin
from aplicacao_programinha.models import Paciente, Atendente, Medico, Sintoma, Consulta


# Register your models here.


admin.site.register(Paciente)
admin.site.register(Atendente)
admin.site.register(Medico)
admin.site.register(Sintoma)
admin.site.register(Consulta)


