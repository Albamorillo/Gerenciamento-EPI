from django.contrib import admin
from django.urls import path
from epi_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('colaboradores/', views.colaboradores_lista, name='colaboradores_lista'),
    path('equipamentos/', views.equipamentos_lista, name='equipamentos_lista'),
    path('usuarios/', views.usuarios_lista, name='usuarios_lista'),
    path('emprestimos/', views.emprestimos_lista, name='emprestimos_lista'),
    path('colaboradores/novo/', views.colaboradores_criar, name='colaboradores_criar'),
    path('equipamentos/novo/', views.equipamentos_criar, name='equipamentos_criar'),
    path('usuarios/novo/', views.usuarios_criar, name='usuarios_criar'),
    path('emprestimos/novo/', views.emprestimos_criar, name='emprestimos_criar'),
    path('colaboradores/<int:pk>/excluir/', views.colaboradores_excluir, name='colaboradores_excluir'),
    path('equipamentos/<int:pk>/excluir/', views.equipamentos_excluir, name='equipamentos_excluir'),
    path('usuarios/<int:pk>/excluir/', views.usuarios_excluir, name='usuarios_excluir'),
    path('emprestimos/<int:pk>/excluir/', views.emprestimos_excluir, name='emprestimos_excluir'),
    path('colaboradores/<int:pk>/editar/', views.colaboradores_editar, name='colaboradores_editar'),
    path('equipamentos/<int:pk>/editar/', views.equipamentos_editar, name='equipamentos_editar'),
    path('usuarios/<int:pk>/editar/', views.usuarios_editar, name='usuarios_editar'),
    path('emprestimos/<int:pk>/editar/', views.emprestimos_editar, name='emprestimos_editar'),
    path('entrar/', views.entrar_view, name='entrar'),
    path('criar-conta/', views.criar_conta_view, name='criar_conta'),
    path('relatorio/', views.relatorio_emprestimos, name='relatorio_emprestimos'),
]