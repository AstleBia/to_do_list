# Generated by Django 5.1.7 on 2025-04-01 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='concluida',
            new_name='concluido',
        ),
    ]
