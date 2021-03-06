# Generated by Django 2.1.7 on 2019-03-04 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_alt',
            field=models.CharField(blank=True, max_length=1200, verbose_name='Texto alternativo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_path',
            field=models.ImageField(default='dummy.jpg', upload_to='media', verbose_name='Endereço da imagem'),
        ),
    ]
