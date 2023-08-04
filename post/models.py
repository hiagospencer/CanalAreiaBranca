from django.db import models

from ckeditor.fields import RichTextField

LISTA_CATEGORIA = (
    ('brasil', 'Brasil'),
    ('rio grande do norte', 'Rio Grande Do Norte'),
    ('areia branca', 'Areia Branca'),
    ('cultura', 'Cultura'),
    ('esporte', 'Esporte'),
    ('política', 'Politica'),
    ('economia', 'Economia'),
    ('entretenimento', 'Entretenimento'),

)
class Post(models.Model):
    titulo = models.CharField(max_length=1000)
    resumo =  models.TextField(max_length=10000000)
    descricao =  RichTextField(max_length=10000000)
    imagem = models.ImageField(upload_to='thumb_img')
    data = models.DateTimeField(auto_now_add = True)
    autor = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30, choices=LISTA_CATEGORIA)

    def __str__(self):
        return self.titulo
