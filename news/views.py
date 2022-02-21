# Quarta Parte do Projeto:

"""
Cada exibição(view) é responsável por fazer uma das 2 coisas: Retornar um 'objeto HttpResponse' com o conteúdo da página solicitada ou gerar uma exceção Http 404.
O resto é com o desenvolvedor.

Geralmente, uma visualização recupera os dados de acordo com os parâmetros, carrega um modelo e renderiza o modelo com os dados recuperados.
"""

from django.shortcuts import render

from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date_year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

"""
Este exemplo usa o sistema de templates do Django, que possui vários recursos poderosos, mas se esforça para permanecer simples o suficiente para 'não-programadores' usarem.
"""
