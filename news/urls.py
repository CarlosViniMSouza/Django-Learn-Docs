# Terceira Parte do Projeto:

"""
Um esquema de URL limpo e elegante é um detalhe importante em um aplicativo da Web de alta qualidade. O Django encoraja um belo design de URL e não coloca nenhuma sujeira em URLs, como .php ou .asp.

Para projetar URLs para um aplicativo, você cria um módulo Python chamado URLconf. Um índice para seu aplicativo, ele contém um mapeamento entre padrões de URL e funções de retorno de chamada do Python.
Os URLconfs também servem para desacoplar URLs do código Python.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('articles/<int:year>', views.year_archive),
    path('articles/<int:year>/<int:month>', views.month_archive),
    path('articles/<int:year>/<int:month>/<int:pk>', views.article_detail),
]

"""
O código acima mapeia caminhos de URL para funções de callback do Python ("views"). As strings de caminho usam tags de parâmetro para "capturar" valores dos URLs. 
Quando um usuário solicita uma página, o Django percorre cada caminho, em ordem, e para no primeiro que corresponde à URL solicitada. 
(Caso não encontre, o Django responde com o 'error 404').

Uma vez que um dos padrões de URL corresponde, o Django chama a visão dada (função do Python). Cada visualização recebe um objeto de solicitação
– que contém metadados de solicitação – e os valores capturados no padrão.

Por exemplo, se um usuário solicitasse a URL "/articles/2005/05/39323/", o Django chamaria a função 'news.views.article_detail(solicitação, ano=2005, mês=5, pk=39323)'.
"""
