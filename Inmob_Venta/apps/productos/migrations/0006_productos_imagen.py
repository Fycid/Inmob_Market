# Generated by Django 3.2.10 on 2022-03-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_productos_detalle'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
