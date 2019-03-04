from django.urls import resolve
from django.test import TestCase

from news.models import Post, Tag
from news.views import home_page


class HomePageTest(TestCase):
    """
    Tests for the home page with list of posts.
    """

    def test_pagina_raiz_resolve_para_view_da_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_pagina_raiz_retona_template_correto(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_pagina_raiz_mostra_todos_os_posts(self):
        tag_arq = Tag.objects.create(name='arquitetura')
        tag_decor = Tag.objects.create(name='decoração')

        post1 = Post.objects.create(title='Notícia 01',
                                    text='Lorem ipsum dolor simet')
        post1.tags.add(tag_arq)
        post1.publish()

        post2 = Post.objects.create(title='Notícia decoração',
                                    text='Lorem ipsum dolor simet')
        post2.tags.add(tag_decor)
        post2.publish()

        post3 = Post.objects.create(title='Arquitetura e decoração',
                                    text='Lorem ipsum dolor')
        post3.tags.add(tag_arq, tag_decor)
        post3.publish()

        response = self.client.get('/')

        self.assertIn(post1.title, response.content.decode())
        self.assertIn(post2.title, response.content.decode())
        self.assertIn(post3.title, response.content.decode())

    def test_pagina_raiz_contem_noticias_com_titulo_e_imagem(self):
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
        self.tag_arq = Tag.objects.create(name='arquitetura')
        self.post1 = Post.objects.create(title='Notícia 01',
                                         text='Lorem ipsum dolor simet')
        self.post1.tags.add(self.tag_arq)
        self.post1.publish()

        response = self.client.get(f'/post/{self.post1.pk}/')

        self.assertIn(self.post1.title, response.content.decode())
        self.assertIn(self.post1.text, response.content.decode())
        self.assertIn(f'<li>{self.tag_arq.name}</li>',
                      response.content.decode())
        self.assertIn('h1', response.content.decode())
        self.assertIn('img', response.content.decode())


class CategoriesPageTest(TestCase):
    """
    Tests for the page with the list of posts for a given category.
    """

    def test_pagina_de_categories_mostra_noticias_da_categoria(self):
        self.tag_arq = Tag.objects.create(name='arquitetura')
        self.post1 = Post.objects.create(title='Notícia 01',
                                         text='Lorem ipsum dolor simet')
        self.post1.tags.add(self.tag_arq)
        self.post1.publish()
        response = self.client.get(f'/categories/{self.tag_arq.pk}/')
        self.assertEqual(response.status_code, 200)


class ModelsTest(TestCase):
    """
    Tests for the models.
    """

    def test_salvando_e_buscando_noticias(self):
        tag_decor = Tag()
        tag_decor.name = 'decoração'
        tag_decor.save()
        tag_planejamento = Tag()
        tag_planejamento.name = 'planejamento'
        tag_planejamento.save()

        news1 = Post()
        news1.title = 'Notícia de arquitetura'
        news1.text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        news1.image_path = 'dummy.png'
        news1.save()
        news1.tags.add(tag_decor)
        news1.save()

        news2 = Post()
        news2.title = 'Outra notícia de arquitetura'
        news2.text = 'Lorem ipsum praesent libero'
        news2.image_path = 'dummy2.png'
        news2.save()
        news2.tags.add(tag_planejamento)
        news2.save()

        news3 = Post()
        news3.title = 'Notícia de arquitetura e de decoração'
        news3.text = 'Lorem ipsum libero'
        news3.save()
        news3.tags.add(tag_planejamento, tag_decor)
        news3.save()

        saved_news = Post.objects.all()
        self.assertEqual(saved_news.count(), 3)

        first_saved_news = Post.objects.get(pk=1)
        second_saved_news = Post.objects.get(pk=2)
        third_saved_news = Post.objects.get(pk=3)

        self.assertEqual(first_saved_news.title,
                         'Notícia de arquitetura')
        self.assertEqual(second_saved_news.title,
                         'Outra notícia de arquitetura')
        self.assertEqual(third_saved_news.title,
                         'Notícia de arquitetura e de decoração')

        self.assertEqual(first_saved_news.text,
                         'Lorem ipsum dolor sit amet,'
                         ' consectetur adipiscing elit.')
        self.assertEqual(second_saved_news.text, 'Lorem ipsum praesent libero')
        self.assertEqual(third_saved_news.text, 'Lorem ipsum libero')

        self.assertEqual(first_saved_news.image_path, 'dummy.png')
        self.assertEqual(second_saved_news.image_path, 'dummy2.png')
        self.assertFalse(bool(third_saved_news.image_path))

        self.assertIn(tag_decor,
                      [tag for tag in first_saved_news.tags.all()])
        self.assertIn(tag_planejamento,
                      [tag for tag in second_saved_news.tags.all()])
        self.assertIn(tag_decor,
                      [tag for tag in third_saved_news.tags.all()])
        self.assertIn(tag_planejamento,
                      [tag for tag in third_saved_news.tags.all()])
