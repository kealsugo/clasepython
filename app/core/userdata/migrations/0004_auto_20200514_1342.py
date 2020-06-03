# Generated by Django 2.2.12 on 2020-05-14 18:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0003_auto_20200513_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detaroles',
            name='AddUser',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='habiuser',
            name='DescHabi',
            field=ckeditor.fields.RichTextField(default='Estudiante', max_length=2000, null=True, verbose_name='Descripcion de la habilidad'),
        ),
        migrations.AlterField(
            model_name='habiuser',
            name='NombHabi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rates',
            name='Porcentaje',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='rates',
            name='UdtHabil',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
