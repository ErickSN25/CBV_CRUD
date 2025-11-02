from django.db import models

class Livros(models.Model):
    nome = models.CharField(max_length=50)
    ano_lancamento = models.IntegerField(null=False, blank=False)
    autor = models.CharField(max_length=50)
    quant_paginas = models.IntegerField()
    disponiveis = models.IntegerField()