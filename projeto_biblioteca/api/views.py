from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from . import serializers
from biblioteca import models


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super(IsAdminUserOrReadOnly, self).has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Autor.objects.all().order_by('id')
    serializer_class = serializers.AuthorSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class DDCViewSet(viewsets.ModelViewSet):
    queryset = models.Cdd.objects.all().order_by('id')
    serializer_class = serializers.DDCSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = models.Editora.objects.all().order_by('id')
    serializer_class = serializers.PublisherSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ReaderViewSet(viewsets.ModelViewSet):
    queryset = models.Leitor.objects.all().order_by('id')
    serializer_class = serializers.ReaderSerializer
    permission_classes = [permissions.IsAdminUser]

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = models.Local_Publicacao.objects.all().order_by('id')
    serializer_class = serializers.PlaceSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Livro.objects.all().order_by('id')
    serializer_class = serializers.BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class CopyViewSet(viewsets.ModelViewSet):
    queryset = models.Exemplar.objects.all().order_by('id')
    serializer_class = serializers.CopySerializer
    permission_classes = [IsAdminUserOrReadOnly]

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = models.Emprestimo.objects.all().order_by('id')
    serializer_class = serializers.BorrowSerializer
    permission_classes = [permissions.IsAdminUser]

class HasAuthorViewSet(viewsets.ModelViewSet):
    queryset = models.LivroTemAutor.objects.all().order_by('id')
    serializer_class = serializers.HasAuthorSerializer
    permission_classes = [IsAdminUserOrReadOnly]
