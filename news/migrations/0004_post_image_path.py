# Generated by Django 2.1.7 on 2019-02-26 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_path',
            field=models.ImageField(default='pic_folder/user/no-img.jpg', upload_to='media', verbose_name='Endereço da imagem'),
        ),
    ]
