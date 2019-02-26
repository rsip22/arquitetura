from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, default='')
    text = models.TextField(default='')
    image_path = models.ImageField('Endereço da imagem',
                                   upload_to='media',
                                   default='pic_folder/user/no-img.jpg')
    tag = models.CharField(max_length=80, default='')

    def __str__(self):
        return self.title
