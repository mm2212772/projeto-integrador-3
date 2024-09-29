# Create your views here.
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from . import forms


def inicial(request):
    return render(request, "inicial.html", context={"guia_atual": "inicial"})


# def leitores(request):
#     if request.method == "GET":
#         leitores = models.Leitor.objects.all()
#     else:
#         pesquisa = request.POST["termos_pesquisa"]
#         leitores = models.Leitor.objects.raw(
#             f" select * from biblioteca_leitor where nome like '%{pesquisa}%'"
#         )
#     context = {
#         "guia_atual": "leitores",
#         "leitores": leitores,
#     }
#     return render(request, "leitores.html", context)


def livros(request):
    return render(request, "livros.html", context={"guia_atual": "livros"})


@login_required(login_url="biblioteca:login")
def devolucoes(request):
    return render(request, "devolucoes.html", context={"guia_atual": "devolucoes"})


# def adicionar_leitor(request):
#     leitor = models.Leitor(
#         nome=request.POST["nome_leitor"],
#         data_nascimento=request.POST["data_nascimento_leitor"],
#     )
#     leitor.save()
#     return redirect("/leitores")


def register(request):
    form = forms.RegisterForm()
    context = {
        "form": form,
    }

    if request.method == "POST":
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuário registrado")
            return redirect("biblioteca:login")

    return render(request, "create_user.html", context)


@login_required(login_url="biblioteca:login")
def user_update(request):
    form = forms.RegisterUpdateForm(instance=request.user)

    if request.method != "POST":
        return render(request, "user_update.html", {"form": form})

    form = forms.RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(request, "user_update.html", {"form": form})

    form.save()
    return redirect("biblioteca:user_update")


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect("biblioteca:inicial")
        else:
            messages.error(request, "Login inválido")

    context = {"form": form}
    return render(request, "login.html", context)


@login_required(login_url="biblioteca:login")
def logout_view(request):
    auth.logout(request)
    return redirect("biblioteca:login")
