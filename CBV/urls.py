from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros/', include('livros.urls')),
    path('', lambda request: redirect('livro_listar')),  # Redireciona para /livros/
]
