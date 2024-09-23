from django.urls import path

from . import views

app_name = "biblioteca"

urlpatterns = [
    path("", views.inicial),
    path("leitores", views.leitores),
    path("livros", views.livros),
    path("sacola", views.sacola),
    path("devolucoes", views.devolucoes),
]
