from django.urls import path
from .views import (
    Livro_listar,
    Livro_detalhar,
    Livro_criar,
    Livro_editar,
    Livro_deletar
)

urlpatterns = [
    path('', Livro_listar.as_view(), name='livro_listar'),
    path('novo/', Livro_criar.as_view(), name='livro_criar'),
    path('<int:pk>/', Livro_detalhar.as_view(), name='livro_detalhar'),
    path('<int:pk>/editar/', Livro_editar.as_view(), name='livro_editar'),
    path('<int:pk>/deletar/', Livro_deletar.as_view(), name='livro_deletar'),
]
