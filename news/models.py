from django.db import models


class Post(models.Model):
    """
    Model for the news articles.
    """
    title = models.CharField(max_length=200, default='')
    text = models.TextField(default='')
    image_path = models.ImageField('Endereço da imagem',
                                   upload_to='media',
                                   default='pic_folder/user/no-img.jpg')
    tag = models.ForeignKey('Tag',
                            related_name='tag',
                            blank=True,
                            on_delete=models.SET_NULL,
                            null=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    """
    Model for the article's tags.
    """
    name = models.CharField(max_length=200, default='')

    def __str__(self):
        return f'{self.name}'
