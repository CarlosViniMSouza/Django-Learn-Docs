# Primeira parte do projeto:

"""
Embora você possa usar o Django sem um banco de dados, ele vem com um mapeador objeto-relacional no qual você descreve seu layout de banco de dados em código Python.

A sintaxe do modelo de dados oferece muitas maneiras ricas de representar seus modelos - até agora, tem resolvido muitos problemas de esquema de banco de dados.

Veja, aqui está um exemplo rápido:
"""

from django.db import models


class Reporter(models.Model):
    name_completed = models.CharField(max_length=100)

    def __str__(self):
        return self.name_completed


class Article(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=20)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Em seguida, execute os utilitários de linha de comando do Django para criar as tabelas de banco de dados automaticamente

"""
$ python manage.py makemigrations
$ python manage.py migrate
"""

# 'makemigrations': analisa todos os seus modelos disponíveis e cria migrações para as tabelas que não já existe.
# 'migrate': executa as migrações e cria tabelas em seu banco de dados, além de fornecer opcionalmente muito mais controle no esquema.

"""
Uma vez que seus modelos são definidos, o Django pode criar automaticamente uma interface administrativa profissional pronta para produção:
 
Um site que permite que usuários autenticados adicionem, alterem e excluam objetos. A única etapa necessária é registrar seu modelo no site de administração.

-> Dirija-se ao arquivo admin.py
"""