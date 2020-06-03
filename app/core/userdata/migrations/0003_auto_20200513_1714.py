# Generated by Django 2.2.12 on 2020-05-13 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_auto_20200513_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosuser',
            name='TeleUser',
            field=models.CharField(max_length=20, verbose_name='telefono usuario'),
        ),
        migrations.AlterField(
            model_name='detaroles',
            name='IDUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.DatosUser', verbose_name='id rol'),
        ),
    ]