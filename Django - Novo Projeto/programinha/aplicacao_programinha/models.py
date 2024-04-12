from django.db import models

class Atendente(models.Model):
    id = models.IntegerField(primary_key=True)
    nome_completo = models.CharField(max_length=100, verbose_name="Nome do atendente", help_text="Informe o nome completo do atendente")
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    data_cadastro = models.DateField(auto_now_add=True)
    data_modificacao = models.DateField(auto_now_add=True)


class Medico(models.Model):
    id = models.IntegerField(primary_key=True)
    nome_completo = models.CharField(max_length=100, verbose_name= 'nome do medico', help_text='Informe o nome completo do médico')
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    especialidade = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    data_cadastro = models.DateField(auto_now_add=True)



class Paciente(models.Model):
    id = models.IntegerField(primary_key=True)
    nome_completo = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    data_cadastro = models.DateField(auto_now_add=True)
    data_modificacao = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.nome_completo
    
class Consulta(models.Model):
    id = models.IntegerField(primary_key=True)
    data_agendamento = models.DateField(auto_now_add=True)
    data_consulta = models.DateField()
    relato_paciente = models.TextField(blank= True)
    sintomas = models.TextField(blank= True)
    laudo = models.TextField(blank=True)
    medicacao = models.CharField(max_length=250, blank=True)
    Paciente = models.ForeignKey(Paciente, on_delete = models.PROTECT)
    atendente = models.ForeignKey(Atendente, on_delete = models.PROTECT)
    medico = models.ForeignKey(Medico, on_delete = models.PROTECT)
        
class Sintoma(models.Model):
    descricao = models.CharField(max_length=100)
    
    
    
    #Comandos de sala de aula
    # blank = True / False
    # verbose_name 
    # help_text
    # max_length
    # auto_now_add
    # auto_now
    # Foreignkey
        #on_delete cascade Protect
    
    #ManytoManyField

def __str__(self):
    return f"Paciente: {self.nome_completo} - {self.email}"

