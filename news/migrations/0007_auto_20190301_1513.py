# Generated by Django 2.1.7 on 2019-03-01 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20190228_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_path',
            field=models.ImageField(default=None, upload_to='media', verbose_name='Endereço da imagem'),
        ),
    ]
