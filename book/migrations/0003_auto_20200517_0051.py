# Generated by Django 3.0.6 on 2020-05-16 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20200515_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='book.AuthorBook'),
        ),
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(blank=True, upload_to='books/', verbose_name='Книга'),
        ),
    ]