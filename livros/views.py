from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Livros
from django.urls import reverse_lazy
from .forms import LivroForm

class Livro_listar(ListView):
    model = Livros
    template_name = 'livros/livro_listar.html'
    context_object_name = 'livro'

class Livro_detalhar(DetailView):
    model = Livros
    template_name = 'livros/livro_detalhar.html'
    context_object_name = 'livro'

class Livro_criar(CreateView):
    model = Livros
    form_class = LivroForm
    template_name = 'livros/livro_criar.html'
    success_url = reverse_lazy('livro_listar')

class Livro_editar(UpdateView):
    model = Livros
    form_class = LivroForm
    template_name = 'livros/livro_editar.html'
    success_url = reverse_lazy('livro_listar') 

class Livro_deletar(DeleteView):
    model = Livros
    template_name = 'livros/livro_deletar.html'
    success_url = reverse_lazy('livro_listar') 
