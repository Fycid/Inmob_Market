# Generated by Django 3.2.10 on 2022-03-17 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_productos_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='Categorias',
        ),
        migrations.AddField(
            model_name='productos',
            name='Categorias',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.categorias'),
        ),
    ]
