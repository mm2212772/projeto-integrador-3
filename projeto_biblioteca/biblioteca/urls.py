from django.urls import path

from . import views

app_name = "biblioteca"

urlpatterns = [
    path("", views.inicial, name="inicial"),
    path("livros", views.livros, name="livros"),
    path("livros/<int:livro_id>/", views.detalhes, name="detalhes"),
    path("user/login/", views.login_view, name="login"),
    path("restrito", views.restrito, name="restrito"),
    path('upload/csv/', views.salvar_leitores, name='upload_csv_leitores'),
]
