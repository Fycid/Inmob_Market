# Generated by Django 3.2.10 on 2022-04-12 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_es_administrador'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(default='', upload_to='usuarios'),
        ),
    ]
