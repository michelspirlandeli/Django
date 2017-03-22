from django.forms import ModelForm
from .models import *
from django.shortcuts import render

# Create your views here.

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['autor','editora', 'isbn', 'numeroPaginas', 'titulo', 'anoPublicacao', 'emailEditora']

def livro_list(request, template_name='livro_list.html'):
    livro = Livro.objects.all()
    livros = {'lista': livro}
    return render(request, template_name, livros)