# Generated by Django 2.2.4 on 2019-08-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190827_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover_pic',
            field=models.ImageField(default='cover-default.jpg', upload_to='cover_pics'),
        ),
    ]
