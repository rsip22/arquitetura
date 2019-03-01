from django.db import models
from django.utils import timezone


class Tag(models.Model):
    """
    Model for the article's tags.
    """
    name = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Model for the news articles.
    """
    title = models.CharField(max_length=200, default='')
    text = models.TextField(default='')
    image_path = models.ImageField('Endereço da imagem',
                                   upload_to='media',
                                   default=None)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag,
                                  related_name='tag',
                                  blank=True,
                                  help_text='Categorias do artigo')

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def show_tags(self):
        return self.tags.all()
