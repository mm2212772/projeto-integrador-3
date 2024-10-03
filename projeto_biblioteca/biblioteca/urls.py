from django.urls import path
from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "biblioteca"

router = routers.DefaultRouter()
router.register(r'usuarios', views.UserViewSet)
router.register(r'autores', views.AuthorViewSet)
router.register(r'livros', views.BookViewSet)
router.register(r'exemplares', views.CopyViewSet)
router.register(r'emprestimos', views.BorrowViewSet)
router.register(r'cdd', views.DDCViewSet)
router.register(r'temautor', views.HasAuthorViewSet)

urlpatterns = [
    path("", views.inicial, name="inicial"),
    path("livros", views.livros, name="livros"),
    path("livros/<int:livro_id>/", views.detalhes, name="detalhes"),
    path("emprestimos", views.emprestimos, name="emprestimos"),
    path("user/create/", views.register, name="register"),
    path("user/login/", views.login_view, name="login"),
    path("user/logout/", views.logout_view, name="logout"),
    path("user/update/", views.user_update, name="user_update"),
    path("api/", include(router.urls)),
    path("api/auth", include('rest_framework.urls', namespace='rest_framework'))
]
