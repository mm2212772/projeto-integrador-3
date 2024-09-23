# Create your views here.
from django.shortcuts import render


def inicial(request):
    return render(request, "inicial.html", context={"guia_atual": "inicial"})


def leitores(request):
    return render(request, "leitores.html", context={"guia_atual": "leitores"})


def livros(request):
    return render(request, "livros.html", context={"guia_atual": "livros"})


def sacola(request):
    return render(request, "sacola.html", context={"guia_atual": "sacola"})


def devolucoes(request):
    return render(request, "devolucoes.html", context={"guia_atual": "devolucoes"})


def salvar_aluno(request):
    nome_aluno = request.POST["nome_aluno"]
    return render(request, "bem-vindo.html", context={"nome_aluno": nome_aluno})
