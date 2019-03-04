from django.urls import resolve
from django.test import TestCase
from django.utils import timezone

from news.models import Post, Tag
from news.views import home_page


class HomePageTest(TestCase):
    """
    Tests for the home page with list of posts.
    """
    fixtures = ['news.json']

    def test_pagina_raiz_resolve_para_view_da_homepage(self):
        """ Test home_page resolves to correct view. """
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_pagina_raiz_retona_template_correto(self):
        """ Test home_page resolves to the correct template. """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_pagina_raiz_mostra_todos_os_posts_publicados(self):
        """ Test querying published news against app fixtures. """
        response = self.client.get('/')

        posts = Post.objects.all(
            ).filter(
            published_date__lte=timezone.now()).order_by('published_date')

        for post in posts:
            self.assertIn(post.title, response.content.decode())

    def test_pagina_raiz_contem_noticias_com_titulo_e_imagem(self):
        """ Test home_page contains news with title and image. """
        self.tag_arq = Tag.objects.create(name='arquitetura')
        self.post1 = Post.objects.create(title='Notícia 01',
                                         text='Lorem ipsum dolor simet')
        self.post1.tags.add(self.tag_arq)
        self.post1.publish()

        response = self.client.get('/')

        self.assertIn(self.post1.text, response.content.decode())
        self.assertIn(self.post1.title, response.content.decode())
        self.assertIn('h2', response.content.decode())
        self.assertIn('img', response.content.decode())


class PostPageTest(TestCase):
    """
    Tests for the post detail page.
    """

    def test_pagina_de_noticia_mostra_noticia(self):
        """ Test post detail page returns one post. """
        self.tag_arq = Tag.objects.create(name='arquitetura')
        self.post1 = Post.objects.create(title='Notícia 01',
                                         text='Lorem ipsum dolor simet')
        self.post1.tags.add(self.tag_arq)
        self.post1.publish()

        response = self.client.get(f'/post/{self.post1.pk}/')

        self.assertIn(self.post1.title, response.content.decode())
        self.assertIn(self.post1.text, response.content.decode())
        self.assertIn(
            f'<li><a href="/categories/{self.tag_arq.pk}/">'
            + f'{self.tag_arq.name}</a></li>',
            response.content.decode())
        self.assertIn('h1', response.content.decode())
        self.assertIn('img', response.content.decode())


class CategoriesPageTest(TestCase):
    """
    Tests for the page with the list of posts for a given category.
    """

    def test_pagina_de_categories_mostra_noticias_da_categoria(self):
        """
        Test categories list returns the list of posts
        belonging to the given category.
        """
        self.tag_arq = Tag.objects.create(name='arquitetura')
        self.post1 = Post.objects.create(title='Notícia 01',
                                         text='Lorem ipsum dolor simet')
        self.post1.tags.add(self.tag_arq)
        self.post1.publish()
        response = self.client.get(f'/categories/{self.tag_arq.pk}/')
        self.assertEqual(response.status_code, 200)


class PostModelTest(TestCase):
    """
    Tests for the models.
    """
    fixtures = ['news.json']

    def test_salvando_e_buscando_noticias(self):
        """ Test querying news against app fixtures. """

        saved_news = Post.objects.all()
        self.assertEqual(saved_news.count(), 3)

        first_saved_news = Post.objects.get(pk=1)
        second_saved_news = Post.objects.get(pk=2)
        third_saved_news = Post.objects.get(pk=3)

        self.assertEqual(first_saved_news.title,
                         'Notícia de arquitetura')
        self.assertEqual(second_saved_news.title,
                         'Notícia de planejamento')
        self.assertEqual(third_saved_news.title,
                         'Notícia de arquitetura e de decoração')

        self.assertEqual(first_saved_news.text,
                         'Lorem ipsum dolor sit amet,'
                         ' consectetur adipiscing elit.')
        self.assertEqual(second_saved_news.text, 'Lorem ipsum praesent libero')
        self.assertEqual(third_saved_news.text, 'Lorem ipsum libero')

        self.assertEqual(first_saved_news.image_path, '/media/media/139.jpg')
        self.assertEqual(second_saved_news.image_path, '/media/media/287.jpg')
        self.assertEqual(third_saved_news.image_path, '/media/media/dummy.jpg')

        self.assertIn('arquitetura',
                      [tag.name for tag in first_saved_news.tags.all()])
        self.assertIn('planejamento',
                      [tag.name for tag in second_saved_news.tags.all()])
        self.assertIn('decoração',
                      [tag.name for tag in third_saved_news.tags.all()])
