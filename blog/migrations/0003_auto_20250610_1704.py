# Generated by Django 3.2.25 on 2025-06-10 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20250610_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacion',
            old_name='imagen_url',
            new_name='imagen',
        ),
        migrations.RenameField(
            model_name='publicacion',
            old_name='texto',
            new_name='introduccion',
        ),
        migrations.AddField(
            model_name='publicacion',
            name='actualidad',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='historia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='puntaje',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
