# Generated by Django 3.2.10 on 2022-03-28 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0012_alter_productos_detalle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='detalle',
            field=models.TextField(default=''),
        ),
    ]
