# Generated by Django 4.2.16 on 2024-09-24 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadastro',
            options={'ordering': ['-data'], 'verbose_name': 'Formulario de Contato', 'verbose_name_plural': 'Formularios de Contato'},
        ),
    ]