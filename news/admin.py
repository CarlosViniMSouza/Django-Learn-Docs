# Segunda Parte do projeto:

"""
Uma vez que seus modelos são definidos, o Django pode criar automaticamente uma interface administrativa profissional pronta para produção:

Um site que permite que usuários autenticados adicionem, alterem e excluam objetos. A única etapa necessária é registrar seu modelo no site de administração.
"""

from django.contrib import admin

from . import models

admin.site.register(models.Article)

"""
Um fluxo de trabalho típico na criação de aplicativos Django é criar modelos e colocar os sites de administração em funcionamento o mais rápido possível,
para que sua equipe (ou clientes) possa começar a preencher os dados. Em seguida, desenvolva a forma como os dados são apresentados ao público.
"""
