# Generated by Django 3.0.6 on 2020-05-20 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200515_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post/', verbose_name='Главная фотография'),
        ),
    ]
