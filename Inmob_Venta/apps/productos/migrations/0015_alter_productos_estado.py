# Generated by Django 3.2.10 on 2022-05-09 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0014_alter_productos_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='Estado',
            field=models.IntegerField(choices=[(1, 'En Venta'), (2, 'Reservado'), (3, 'Vendido'), (4, 'En Alquiler'), (5, 'Alquilado')], default=1),
        ),
    ]
