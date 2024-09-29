from django.urls import path

from . import views

app_name = "biblioteca"

urlpatterns = [
    path("", views.inicial, name="inicial"),
    # path("leitores", views.leitores, name="leitores"),
    # path("leitores/adicionar", views.adicionar_leitor, name="adicionar_leitor"),
    path("livros", views.livros, name="livros"),
    path("livros/<int:livro_id>/", views.detalhes, name="detalhes"),
    path("emprestimos", views.emprestimos, name="emprestimos"),
    path("user/create/", views.register, name="register"),
    path("user/login/", views.login_view, name="login"),
    path("user/logout/", views.logout_view, name="logout"),
    path("user/update/", views.user_update, name="user_update"),
]
