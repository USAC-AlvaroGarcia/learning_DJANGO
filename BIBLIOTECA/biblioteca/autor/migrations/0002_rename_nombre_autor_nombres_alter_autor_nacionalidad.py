# Generated by Django 4.0.4 on 2022-05-29 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='nombre',
            new_name='nombres',
        ),
        migrations.AlterField(
            model_name='autor',
            name='nacionalidad',
            field=models.CharField(max_length=20),
        ),
    ]
