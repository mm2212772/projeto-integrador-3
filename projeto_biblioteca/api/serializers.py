from biblioteca import models
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ( "id", "username", "first_name", "last_name", "email", "is_active", "is_staff", "is_superuser", "date_joined", "last_login")

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Autor
        fields = ("id", "nome", "codigo_autor")


class DDCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Cdd
        fields = ("id", "nome")


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Editora
        fields = ("id", "nome")


class ReaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Leitor
        fields = ("id", "nome", "ra", "ativo")


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Local_Publicacao
        fields = ("id", "nome")


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Livro
        fields = ("id", "titulo", "subtitulo", "ano", "edicao", "isbn", "iniciais_titulo", "cdd_id", "editora_id", "local_publicacao_id")


class CopySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Exemplar
        fields = ("id", "livro_id", "tombo", "numero_exemplar", "etiqueta_gerada", "baixa", "motivo_baixa")


class BorrowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Emprestimo
        fields = ( "id", "leitor_id", "exemplar_id", "data_emprestimo", "data_devolucao", "devolvido")


class HasAuthorSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = models.LivroTemAutor
        fields = ("id", "autor_id", "livro_id")
