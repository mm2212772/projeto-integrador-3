# Generated by Django 5.1.1 on 2024-09-29 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("biblioteca", "0002_alter_emprestimo_data_devolucao"),
    ]

    operations = [
        migrations.RenameField(
            model_name="emprestimo",
            old_name="livro",
            new_name="exemplar",
        ),
    ]
