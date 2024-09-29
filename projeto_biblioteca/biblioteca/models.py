# Create your models here.
from datetime import timedelta

from django.contrib.auth.models import User  # type:ignore
from django.db import models  # type:ignore
from django.utils import timezone  # type:ignore


class Cdd(models.Model):
    class Meta:
        verbose_name = "cdd"

    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=100)


class Autor(models.Model):
    class Meta:
        verbose_name = "autor"
        verbose_name_plural = "autores"

    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=100)


class Livro(models.Model):
    class Meta:
        verbose_name = "livro"
        verbose_name_plural = "livros"

    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    edicao = models.IntegerField()
    quantidade = models.IntegerField()
    volume = models.IntegerField()
    cdd = models.ForeignKey(Autor, on_delete=models.SET_NULL, blank=True, null=True)


class Livro_tem_autor(models.Model):
    class Meta:
        verbose_name = "livro_tem_autor"
        verbose_name_plural = "livro_tem_autores"

    def __str__(self):
        return f"Autor: {self.autor.nome}, Livro: {self.livro.nome}"

    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, blank=True, null=True)
    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, blank=True, null=True)


class Emprestimo(models.Model):
    class Meta:
        verbose_name = "emprestimo"
        verbose_name_plural = "emprestimos"

    def __str__(self):
        return f"Leitor: {User.first_name} {User.last_name}, Livro: {self.livro.nome}"

    leitor = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, blank=True, null=True)
    data_emprestimo = models.DateField(default=timezone.now)
    data_devolucao = models.DateField(
        default=lambda: timezone.now() + timedelta(weeks=1)
    )
    devolvido = models.BooleanField(default=False)
