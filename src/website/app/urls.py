#rotas do app 


from django.urls import path
from .views import AlunoListView, AlunoCreateView, AlunoUpdateView, AlunoDeleteView
from .views import InstrutorCreateView, InstrutorDeleteView, InstrutorUpdateView, InstrutorListView
from .views import TurmaCreateView, TurmaListView, TurmaUpdateView, TurmaDeleteView
from .views import CursoCreateView, CursoDeleteView, CursoListView, CursoUpdateView
from .views import CicloListView, CicloCreateView, CicloDeleteView, CicloUpdateView
from .import views



urlpatterns = [
    path("", views.index, name="index"),
    path('home/', views.home, name='home'),
    #aluno
    path("alunos/", AlunoListView.as_view(), name="aluno_list"),
    path("alunos/novo/", AlunoCreateView.as_view(), name="aluno_create"),
    path("alunos/<int:pk>/editar/", AlunoUpdateView.as_view(), name="aluno_update"),
    path("alunos/<int:pk>/deletar/", AlunoDeleteView.as_view(), name="aluno_delete"),
    #instrutor
    path("instrutores/", InstrutorListView.as_view(), name="instrutor_list"),
    path("instrutores/novo/", InstrutorCreateView.as_view(), name="instrutor_create"),
    path("instrutores/<int:pk>/editar", InstrutorUpdateView.as_view(), name="instrutor_update"),
    path("instrutoes/<int:pk>/deletar", InstrutorDeleteView.as_view(), name="instrutor_delete"),
    #turma
    path("turmas/", TurmaListView.as_view(),name="turma_list"),
    path("turmas/novo/", TurmaCreateView.as_view(), name="turma_create"),
    path("turmas/<int:pk>/editar/", TurmaUpdateView.as_view(), name="turma_update"),
    path("turmas/<int:pk>/deletar/", TurmaDeleteView.as_view(), name="turma_delete"),
    #curso
    path("cursos/", CursoListView.as_view(), name="curso_list"),
    path("cursos/novo/", CursoCreateView.as_view(), name="curso_create"),
    path("cursos/<int:pk>/editar/", CursoUpdateView.as_view(), name="curso_update"),
    path("cursos/<int:pk>/deletar/", CursoDeleteView.as_view(), name="curso_delete"),

     #ciclo
    path("ciclos/", CicloListView.as_view(), name="ciclo_list"),
    path("ciclos/novo/", CicloCreateView.as_view(), name="ciclo_create"),
    path("ciclos/<int:pk>/editar/", CicloUpdateView.as_view(), name="ciclo_update"),
    path("ciclos/<int:pk>/deletar/", CicloDeleteView.as_view(), name="ciclo_delete"),

    #relatórios
    path('relatorios/turmas-alunos/', views.relatorio_turma_aluno, name='relatorio_turma_aluno'),
    path('relatorios/cursos-turmas/', views.relatorio_curso_turmas_abertas, name='relatorio_curso_turma_abertas'),
    path('relatorios/turmas-selecionadas/', views.relatorio_turma_selecionada, name='relatorio_turma_selecionada'),

] 
