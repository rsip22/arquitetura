from django.urls import resolve
from django.test import TestCase

from news.models import Post, Tag
from news.views import home_page


class HomePageTest(TestCase):

    def test_pagina_raiz_resolve_para_view_da_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_pagina_raiz_retona_template_correto(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_pagina_raiz_contem_noticias_com_titulo_e_imagem(self):
        response = self.client.get('/')
        self.assertIn('Notícia de arquitetura', response.content.decode())
        self.assertIn('h2', response.content.decode())
        self.assertIn('img', response.content.decode())


class NewsModelTest(TestCase):

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
        news1.tag = tag_decor
        news1.save()

        news2 = Post()
        news2.title = 'Outra notícia de arquitetura'
        news2.text = 'Lorem ipsum praesent libero'
        news2.image_path = 'dummy2.png'
        news2.tag = tag_planejamento
        news2.save()

        saved_news = Post.objects.all()
        self.assertEqual(saved_news.count(), 2)

        first_saved_news = saved_news[0]
        second_saved_news = saved_news[1]

        self.assertEqual(first_saved_news.title,
                         'Notícia de arquitetura')
        self.assertEqual(second_saved_news.title,
                         'Outra notícia de arquitetura')

        self.assertEqual(first_saved_news.text,
                         'Lorem ipsum dolor sit amet,'
                         ' consectetur adipiscing elit.')
        self.assertEqual(second_saved_news.text, 'Lorem ipsum praesent libero')

        self.assertEqual(first_saved_news.image_path, 'dummy.png')
        self.assertEqual(second_saved_news.image_path, 'dummy2.png')

        self.assertEqual(first_saved_news.tag, tag_decor)
        self.assertEqual(second_saved_news.tag, tag_planejamento)
