# Generated by Django 3.2.10 on 2022-03-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_productos_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='estado',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
