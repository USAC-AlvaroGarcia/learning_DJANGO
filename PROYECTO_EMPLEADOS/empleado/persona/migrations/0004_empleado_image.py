# Generated by Django 4.0.4 on 2022-05-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_empleado_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
