from django.contrib import admin

from . import models

# Register your models here.


class LivroAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "ano", "edicao")
    search_fields = ("nome",)
    list_filter = ("nome", "ano")
    ordering = ("id",)
    list_per_page = 20


class CddAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    ordering = ("id",)
    list_per_page = 20


class AutorAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_per_page = 20
    ordering = ("id",)


class LivroTemAutorAdmin(admin.ModelAdmin):
    list_display = ("id", "autor", "livro")
    ordering = ("id",)
    list_per_page = 20


class ExemplarAdmin(admin.ModelAdmin):
    list_display = ("id", "livro")
    ordering = ("id",)
    list_per_page = 20


class EmprestimoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "leitor",
        "exemplar",
        "data_emprestimo",
        "data_devolucao",
        "devolvido",
    )
    list_per_page = 20
    ordering = ("id",)


admin.site.register(models.Cdd, CddAdmin)
admin.site.register(models.Autor, AutorAdmin)
admin.site.register(models.Livro, LivroAdmin)
admin.site.register(models.LivroTemAutor, LivroTemAutorAdmin)
admin.site.register(models.Emprestimo, EmprestimoAdmin)
admin.site.register(models.Exemplar, ExemplarAdmin)
