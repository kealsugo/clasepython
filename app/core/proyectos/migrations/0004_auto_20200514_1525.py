# Generated by Django 2.2.12 on 2020-05-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_auto_20200514_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='ImgProye',
            field=models.ImageField(default='proye.png', upload_to='imgproyecto/img', verbose_name='imagen proyecto'),
        ),
    ]
