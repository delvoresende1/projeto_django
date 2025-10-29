from django import forms
from .models import Aluno
from .models import Turma
from .models import Curso
from .models import Instrutor
from .models import Ciclo

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['matricula', 'nome_aluno', 'cpf_aluno', 'email_aluno', 'endereco', 'telefone', 'data_nascimento', 'turma']
        widgets = {
            'nome_aluno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do Aluno'}),
            'matricula': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Matricula'}),
            'cpf_aluno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'CPF'}),
            'email_aluno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'endereco': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Endereço'}),
            #'data_nascimento': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Data de Nascimento'}),
            # campo telefone com máscara simples
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000',
                'pattern': r'\(\d{2}\) \d{5}-\d{4}',  # validação HTML5
                'title': 'Formato esperado: (99) 99999-9999'
            }),
            # campo data com input type date
            'data_nascimento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                },
                format='%Y-%m-%d'
            ),
            'turma': forms.Select(attrs={'class':'form-control'}),
            
        }

TURNO_CHOICES = (
    ('manha', 'Manhã'),
    ('tarde', 'Tarde'),
    ('noite', 'Noite'),
)
#se a turma já iniciou e se finalizaou
STATUS_CHOICES = (
    ('inicio', 'Iniciada'),
    ('fim', 'Finalizada'),
)
        

class TurmaForm(forms.ModelForm):
    turno = forms.ChoiceField(
        choices=TURNO_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'})
    )
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'})
    )
    class Meta:
        model = Turma
        fields = ['nome_turma', 'turno', 'curso', 'ciclo']
        widgets = {
            'nome_turma': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome da Turma'}),
            #'turno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'turno'}),
            'curso': forms.Select(attrs={'class':'form-control'}),
            'ciclo': forms.Select(attrs={'class':'form-control'}),
        }
#para fazer a requisição de turmas com alunos matriculados
#para preecher o campo select do form
class SelecionaTurmaForm(forms.Form):
    nome_turma = forms.ModelChoiceField(
        queryset=Turma.objects.all().order_by('nome_turma'),
        label='Selecione a Turma',
        empty_label = 'Selecione a Turma',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome_curso', 'carga_horaria', 'descricao_curso']
        widgets = {
            'nome_curso': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do Curso'}),
            'carga_horaria': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Carga Horária'}),
            'descricao_curso': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descrição do Curso'}),
        }


class InstrutorForm(forms.ModelForm):
    class Meta:
        model = Instrutor
        fields = ['cpf_instrutor', 'nome_instrutor', 'email_instrutor', 'endereco', 'telefone', 'data_nascimento', 'especialidade']
        widgets = {
            'cpf_instrutor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'CPF'}),
            'nome_instrutor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do Instrutor'}),
            'email_instrutor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'endereco': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Endereço'}),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000',
                'pattern': r'\(\d{2}\) \d{5}-\d{4}',  # validação HTML5
                'title': 'Formato esperado: (99) 99999-9999'
            }),
            # campo data com input type date
            'data_nascimento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                },
                format='%Y-%m-%d'
            ),
            'especialidade': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Especialidade'}),
        }

class CicloForm(forms.ModelForm):
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'})
    )
    class Meta:
        model = Ciclo
        fields = ['nome_ciclo', 'data_inicio', 'data_fim', 'descricao_ciclo', 'status', 'ano_referencia']
        widgets = {
            'nome_ciclo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do Ciclo'}),
            'data_inicio': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                },
                format='%Y-%m-%d'
            ),
            'data_fim': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                },
                format='%Y-%m-%d'
            ),
            'descricao_ciclo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descrição do Ciclo'}),
            'ano_referencia': forms.NumberInput(attrs={'class':'form-control'})
        }
                 
#turma é campo obrigatório na cadastro do aluno
#curso é obrigatório no cadastro da turma

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['turma'].required = True
    self.fields['curso'].required = True
    #adiciona class bootstrap a todos os campos
    for field_name, field in self.fields.items():
        field.widget.attrs['class'] = 'form-control'
        # garante que o select de turma carregue os dados do banco
    self.fields['turma'].queryset = Turma.objects.all().order_by('descricao_turma')
    self.fields['turma'].empty_label = "Selecione uma Turma"
    self.fields['curso'].queryset = Turma.objects.all().order_by('nome_curso')
    self.fields['curso'].empty_label = "Selecione um curso"
    self.fields['ciclo'].queryset = Turma.objects.all().order_by('nome_ciclo')
    self.fields['ciclo'].empty_label = "Selecione um ciclo"
   