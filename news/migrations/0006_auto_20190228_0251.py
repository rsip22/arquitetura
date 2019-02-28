# Generated by Django 2.1.7 on 2019-02-28 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_post_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tag', to='news.Tag'),
        ),
    ]
