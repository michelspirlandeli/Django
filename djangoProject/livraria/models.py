from django.db import models

# Create your models here.

class Livro (models.Model):
    autor = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    isbn = models.IntegerField()
    numeroPaginas = models.IntegerField()
    titulo = models.CharField(max_length=50)
    anoPublicacao = models.IntegerField()
    emailEditora = models.EmailField()