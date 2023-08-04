from django.urls import path
from .views import (Homepage, DetailPost, PageBrasil,PageCultura,
            PageRN, PageAreiaBranca, PageEsportes,PagePolitica, PageEconomia, PageEntretenimento)


app_name = 'post'
urlpatterns = [
    path("", Homepage.as_view(), name='home'),
    path("categoria/brasil/", PageBrasil.as_view(), name='brasil'),
    path("categoria/riograndedonorte/", PageRN.as_view(), name='rn'),
    path("categoria/areiabranca/", PageAreiaBranca.as_view(), name='areiabranca'),
    path("categoria/cultura/", PageCultura.as_view(), name='cultura'),
    path("categoria/esportes/", PageEsportes.as_view(), name='esportes'),
    path("categoria/politica/", PagePolitica.as_view(), name='politica'),
    path("categoria/economia/", PageEconomia.as_view(), name='economia'),
    path("categoria/entretenimento/", PageEntretenimento.as_view(), name='entretenimento'),

    path('detalhes/<int:pk>', DetailPost.as_view(), name='detalhes'),
]
