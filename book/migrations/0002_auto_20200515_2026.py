# Generated by Django 3.0.6 on 2020-05-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='ФИО наследника')),
                ('image', models.ImageField(blank=True, null=True, upload_to='heir/', verbose_name='Фото наследника')),
                ('text', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Наследник',
                'verbose_name_plural': 'Наследники',
            },
        ),
        migrations.AlterField(
            model_name='authorbook',
            name='text',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
