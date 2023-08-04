from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post


class Homepage(ListView):
    template_name = 'index.html'
    model = Post
    paginate_by = 10
    context_object_name = 'post_home'

    def get_queryset(self):
        return Post.objects.filter().order_by('-data')



class PageBrasil(ListView):
    template_name = 'brasil.html'
    model = Post
    paginate_by = 10
    context_object_name = 'categoria_brasil'

    def get_queryset(self):
        return Post.objects.filter(categoria='brasil').order_by('-data')


class PageRN(ListView):
    template_name = 'riograndedonorte.html'
    model = Post
    paginate_by = 10
    context_object_name = 'categoria_RN'

    def get_queryset(self):
        return Post.objects.filter(categoria='rio grande do norte').order_by('-data')


class PageAreiaBranca(ListView):
    template_name = 'areiabranca.html'
    model = Post
    paginate_by = 10
    context_object_name = 'categoria_areia_branca'

    def get_queryset(self):
        return Post.objects.filter(categoria='areia branca').order_by('-data')


class PageCultura(ListView):
    template_name = 'cultura.html'
    model = Post
    paginate_by = 10
    context_object_name = 'categoria_cultura'

    def get_queryset(self):
        return Post.objects.filter(categoria='cultura').order_by('-data')


class PageEsportes(ListView):
    template_name = 'esportes.html'
    model = Post
    paginate_by = 10
    context_object_name = 'categoria_esportes'

    def get_queryset(self):
        return Post.objects.filter(categoria='esporte').order_by('-data')


class PagePolitica(ListView):
    template_name = 'politica.html'
    model = Post
    paginate_by = 10
    context_object_name = 'categoria_politica'

    def get_queryset(self):
        return Post.objects.filter(categoria='política').order_by('-data')


class PageEconomia(ListView):
    template_name = 'economia.html'
    model = Post
    paginate_by = 10
    context_object_name = 'categoria_economia'

    def get_queryset(self):
        return Post.objects.filter(categoria='economia').order_by('-data')


class PageEntretenimento(ListView):
    template_name = 'entretenimento.html'
    model = Post
    paginate_by = 10
    context_object_name = 'categoria_entretenimento'

    def get_queryset(self):
        return Post.objects.filter(categoria='entretenimento').order_by('-data')


class DetailPost(DetailView):
    template_name = 'detalhes.html'
    model = Post
