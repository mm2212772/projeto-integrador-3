# Create your views here.
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

from . import forms, models

from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from . import serializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]

class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Livro.objects.all().order_by('id')
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Autor.objects.all().order_by('id')
    serializer_class = serializers.AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DDCViewSet(viewsets.ModelViewSet):
    queryset = models.Cdd.objects.all().order_by('id')
    serializer_class = serializers.DDCSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CopyViewSet(viewsets.ModelViewSet):
    queryset = models.Exemplar.objects.all().order_by('id')
    serializer_class = serializers.CopySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class HasAuthorViewSet(viewsets.ModelViewSet):
    queryset = models.LivroTemAutor.objects.all().order_by('id')
    serializer_class = serializers.HasAuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = models.Emprestimo.objects.all().order_by('id')
    serializer_class = serializers.BorrowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def inicial(request):
    return render(request, "inicial.html", context={"guia_atual": "inicial"})


def livros(request):
    if request.method == "GET":
        livros = models.Livro.objects.all()
    else:
        pesquisa = request.POST["termos_pesquisa"]
        livros = models.Livro.objects.raw(
            f" select * from biblioteca_livro where nome like '%{pesquisa}%'"
        )
    context = {"guia_atual": "Livros", "livros": livros}
    return render(request, "livros.html", context)


def detalhes(request, livro_id):
    livro = get_object_or_404(models.Livro, id=livro_id)
    exemplares = models.Exemplar.objects.filter(livro=livro)
    autores = livro.livro_tem_autor_set.select_related("autor")
    context = {
        "guia_atual": "Livros",
        "livro": livro,
        "exemplares": exemplares,
        "autores": autores,
    }
    return render(request, "detalhes.html", context)


@login_required(login_url="biblioteca:login")
def emprestimos(request):
    emprestimos = models.Emprestimo.objects.filter(leitor=request.user)
    context = {"guia_atual": "Empréstimos", "emprestimos": emprestimos}
    return render(request, "emprestimos.html", context)


def register(request):
    form = forms.RegisterForm()
    context = {
        "guia_atual": "Cadastrar",
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
        return render(
            request, "user_update.html", {"guia_atual": "Perfil", "form": form}
        )

    form = forms.RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request, "user_update.html", {"guia_atual": "Perfil", "form": form}
        )

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

    context = {"form": form, "guia_atual": "Login"}
    return render(request, "login.html", context)


@login_required(login_url="biblioteca:login")
def logout_view(request):
    auth.logout(request)
    return redirect("biblioteca:login")
