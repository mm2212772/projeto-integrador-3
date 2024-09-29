# Create your models here.

from datetime import timedelta  # Importa a biblioteca timedelta

from django.contrib.auth.models import User  # type:ignore
from django.db import models  # type:ignore
from django.utils import timezone  # type:ignore


# Função para calcular a data de devolução padrão (hoje + 7 dias)
def get_default_return_date():
    return timezone.now() + timedelta(days=7)


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
    volume = models.IntegerField()
    cdd = models.ForeignKey(Cdd, on_delete=models.SET_NULL, blank=True, null=True)


class LivroTemAutor(models.Model):
    class Meta:
        verbose_name = "livro_tem_autor"
        verbose_name_plural = "livro_tem_autores"

    def __str__(self):
        return f"Autor: {self.autor.nome}, Livro: {self.livro.nome}"

    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, blank=True, null=True)
    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, blank=True, null=True)


class Exemplar(models.Model):
    class Meta:
        verbose_name = "exemplar"
        verbose_name_plural = "exemplares"

    def __str__(self):
        return f"{self.id}: {self.livro.nome}"

    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, blank=True, null=True)


class Emprestimo(models.Model):
    class Meta:
        verbose_name = "emprestimo"
        verbose_name_plural = "emprestimos"

    def __str__(self):
        return f"Leitor: {self.leitor.username}, Livro: {self.exemplar.livro.nome}"

    leitor = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    exemplar = models.ForeignKey(
        Exemplar, on_delete=models.SET_NULL, blank=True, null=True
    )
    data_emprestimo = models.DateField(default=timezone.now)
    data_devolucao = models.DateField(
        default=get_default_return_date
    )  # Define a data de devolução padrão
    devolvido = models.BooleanField(default=False)
