from django.contrib.auth.models import User
from . import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "password", "last_login", "is_superuser", "username",
                  "last_name" , "email", "is_staff", "is_active",
                  "date_joined", "first_name"]

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Livro
        fields = ["id", "nome", "ano", "edicao", "volume", "cdd_id"]

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Autor
        fields = ["id" , "nome"]

class DDCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Cdd
        fields = ["id", "nome"]

class CopySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Exemplar
        fields = ["id", "livro_id"]

class HasAuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.LivroTemAutor
        fields = ["id", "autor_id", "livro_id"]

class BorrowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Emprestimo
        fields = ["id", "data_emprestimo", "data_devolucao", "devolvido",
                  "leitor_id", "exemplar_id"]
