📘 CRUD de Livros com Django

Esse projeto é um sistema simples de CRUD de livros feito com Django usando Class-Based Views (CBVs).
Ele serve pra cadastrar livros, ver detalhes, editar e excluir registros de forma fácil.

🚀 Funcionalidades

Listar todos os livros

Ver detalhes de cada livro

Adicionar um livro novo

Editar um livro existente

Excluir um livro

🌐 Rotas principais

/livros/ → lista todos os livros

/livros/criar/ → formulário pra criar um novo livro

/livros/<id>/ → detalhes de um livro específico

/livros/<id>/editar/ → editar as informações de um livro

/livros/<id>/deletar/ → excluir um livro

🧱 Views usadas

Livro_listar → lista os livros

Livro_detalhar → mostra detalhes de um livro

Livro_criar → cria um livro novo

Livro_editar → edita um livro

Livro_deletar → exclui um livro

🗃️ Modelo de dados

O modelo Livros tem os campos:

nome → nome do livro

ano_lancamento → ano que foi lançado

autor → nome do autor


<img width="1918" height="978" alt="image" src="https://github.com/user-attachments/assets/0ecfb98e-dbc7-4389-8deb-8875a45e3ad5" />
Listagem

<img width="1918" height="918" alt="image" src="https://github.com/user-attachments/assets/cb5c8ff2-ae80-4f3f-bff4-41038f3ec795" />
Criação

<img width="1917" height="920" alt="image" src="https://github.com/user-attachments/assets/6b904aec-50bb-4d40-86ec-eaf8fabc8812" />
Detalhar

<img width="1895" height="896" alt="image" src="https://github.com/user-attachments/assets/21edfd13-b627-49f7-bdef-bb61f9b7d9f2" />
Editar

<img width="1918" height="911" alt="image" src="https://github.com/user-attachments/assets/3b548f5c-3cfc-4246-9229-bb300b69f29d" />
Deletar

quant_paginas → número de páginas

disponiveis → quantidade de exemplares disponíveis
