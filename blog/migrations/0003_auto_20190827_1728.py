# Generated by Django 2.2.4 on 2019-08-27 14:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_pic',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Kapak Fotoğrafı'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('TR', 'TRAVEL'), ('MT', 'MOVIE-SERIES'), ('BK', 'BOOK'), ('GM', 'GAME'), ('CD', 'CODING'), ('AV', 'AVIATION')], default='TR', max_length=2, verbose_name='Kategoriler'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Başlık'),
        ),
    ]
