#VIEWS DO CRUD 

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Aluno
from .models import Instrutor
from .models import Turma
from .models import Curso
from .models import Ciclo
from .forms import AlunoForm
from .forms import TurmaForm
from .forms import CursoForm
from .forms import InstrutorForm
from .forms import CicloForm
from .forms import SelecionaTurmaForm
from django.http import HttpResponse


def index(request):
    return HttpResponse("Página inicial do aplicativo")
    
def home(request):
    return render(request, 'app/home.html')

class AlunoListView(ListView):
    model = Aluno
    template_name = "app/aluno_list.html"
    context_object_name = "alunos"

class InstrutorListView(ListView):
    model = Instrutor
    template_name = "app/instrutor_list.html"
    context_object_name = "instrutores"


class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = "app/aluno_form.html"
    success_url = reverse_lazy("aluno_list")

class InstrutorCreateView(CreateView):
    model = Instrutor
    form_class = InstrutorForm
    template_name = "app/instrutor_form.html"
    success_url = reverse_lazy("instrutor_list")



class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = "app/aluno_form.html"
    success_url = reverse_lazy("aluno_list")

class InstrutorUpdateView(UpdateView):
    model = Instrutor
    form_class = InstrutorForm
    template_name = "app/instrutor_form.html"
    success_url = reverse_lazy("instrutor_list")


class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = "app/aluno_confirm_delete.html"
    success_url = reverse_lazy("aluno_list")

class InstrutorDeleteView(DeleteView):
    model = Instrutor
    template_name = "app/instrutor_confirm_delete.html"
    success_url = reverse_lazy("instrutor_list")

class TurmaListView(ListView):
    model = Turma
    template_name = "app/turma_list.html"
    context_object_name = "turmas"
    ordering = ['nome_turma']

class TurmaCreateView(CreateView):
    model = Turma
    form_class = TurmaForm
    template_name = "app/turma_form.html"
    success_url = reverse_lazy("turma_create")

class TurmaUpdateView(UpdateView):
    model = Turma
    form_class = TurmaForm
    template_name = "app/turma_form.html"
    success_url = reverse_lazy("turma_list")

class TurmaDeleteView(DeleteView):
    model = Turma
    template_name = "app/turma_confirm_delete.html"
    success_url = reverse_lazy("turma_list")

class CursoListView(ListView):
    model = Curso
    template_name = "app/curso_list.html"
    context_object_name = "cursos"

class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = "app/curso_form.html"
    success_url = reverse_lazy("curso_create")

class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = "app/curso_form.html"
    success_url = reverse_lazy("curso_list")

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "app/curso_confirm_delete.html"
    context_object_name = "curso_list"

## CICLO
class CicloListView(ListView):
    model = Ciclo
    template_name = "app/ciclo_list.html"
    context_object_name = "ciclos"

class CicloCreateView(CreateView):
    model = Ciclo
    form_class = CicloForm
    template_name = "app/ciclo_form.html"
    success_url = reverse_lazy("ciclo_create")

class CicloUpdateView(UpdateView):
    model = Ciclo
    form_class = CicloForm
    template_name = "app/ciclo_form.html"
    success_url = reverse_lazy("ciclo_list")

class CicloDeleteView(DeleteView):
    model = Ciclo
    template_name = "app/ciclo_confirm_delete.html"
    context_object_name = "ciclo_list"

#consulta para trazer todas as turmas
# .objects.prefetch_related -> para relacionamentos que retornam um conjunto de objetos
def relatorio_turma_aluno(request):
    # busca todas as turmas com seus alunos
    turmas = Turma.objects.prefetch_related('alunos').all()
    context = {'turmas': turmas}
    return render(request, 'app/relatorio_turma_aluno.html', context)

#busca todos os cursos com turmas abertas
def relatorio_curso_turmas_abertas(request):
    cursos = Curso.objects.prefetch_related('turmas').all()
    context={'cursos':cursos}
    return render(request, 'app/relatorio_curso_turma_aberta.html', context)

#relatorio busca por turma específica com alunos matriculados

def relatorio_turma_selecionada(request):
    turma_selecionada = None
    alunos = None

    # formulário de seleção de turma
    if request.method == 'POST':
        form = SelecionaTurmaForm(request.POST)
        if form.is_valid():
            turma_selecionada = form.cleaned_data['nome_turma']
            alunos = turma_selecionada.alunos.all()
        else: 
            print('form invalido', form.errors)
    else:
        form = SelecionaTurmaForm()

    context = {
        'form': form,
        'turma': turma_selecionada,
        'alunos': alunos
    }
    return render(request, 'app/relatorio_turma_selecionada.html', context)



