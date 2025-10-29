# classes do projeto

from django.db import models

class Curso(models.Model):
    nome_curso = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    descricao_curso = models.TextField()
    

    def __str__(self):
        return self.nome_curso
class Ciclo(models.Model):
    nome_ciclo = models.CharField(max_length=50)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao_ciclo = models.CharField(max_length=100)
    status = models.CharField(max_length=30)
    ano_referencia = models.IntegerField()

    def __str__(self):
        return self.nome_ciclo
    
    

class Turma(models.Model):
    nome_turma = models.CharField(max_length=50)
    turno = models.CharField(max_length=20)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name="turmas")
    ciclo = models.ForeignKey(Ciclo, on_delete=models.PROTECT, related_name="turmas")

    def __str__(self):
        return self.nome_turma

class Instrutor(models.Model):
    cpf_instrutor = models.CharField(max_length=11, unique=True)
    nome_instrutor = models.CharField(max_length=100)
    email_instrutor = models.EmailField()
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_instrutor

class Aluno(models.Model):
    matricula = models.IntegerField(unique=True)
    cpf_aluno = models.CharField(max_length=15, unique=True)
    nome_aluno = models.CharField(max_length=100)
    email_aluno = models.EmailField()
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField() 
    #FK id_turma 
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT, related_name="alunos")
    


    def __str__(self):
        return self.nome_aluno

class InstrutorTurma(models.Model):
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    horario_turma = models.DateTimeField()
    data_inicio = models.DateField()

    class Meta:
        unique_together = ("instrutor", "turma")

class Avaliacao(models.Model):
    data = models.DateField()
    tipo = models.CharField(max_length=50)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="avaliacoes")

    def __str__(self):
        return f"{self.tipo} - {self.data}"

