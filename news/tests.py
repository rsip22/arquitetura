from django.urls import resolve
from django.test import TestCase

from news.models import Post
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
        news1 = Post()
        news1.title = 'Notícia de arquitetura'
        news1.text = '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Integer nec odio. Praesent libero. Sed cursus ante dapibus diam.
            Sed nisi. Nulla quis sem at nibh elementum imperdiet.
            Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed
            augue semper porta. Mauris massa. Vestibulum lacinia arcu
            eget nulla. Class aptent taciti sociosqu ad litora torquent
            per conubia nostra, per inceptos himenaeos. Curabitur sodales
            ligula in libero.
        '''
        news1.img = 'dummy.png'
        news1.tag = 'decoração'
        news1.save()

        news2 = Post()
        news2.title = 'Outra notícia de arquitetura'
        news2.text = '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Integer nec odio. Praesent libero. Sed cursus ante dapibus diam.
            Sed nisi. Nulla quis sem at nibh elementum imperdiet.
            Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed
            augue semper porta. Mauris massa. Vestibulum lacinia arcu
            eget nulla. Class aptent taciti sociosqu ad litora torquent
            per conubia nostra, per inceptos himenaeos. Curabitur sodales
            ligula in libero.
        '''
        news2.img = 'dummy2.png'
        news2.tag = 'planejamento'
        news2.save()

        saved_news = Post.objects.all()
        self.assertEqual(saved_news.count(), 2)

        first_saved_news = saved_news[0]
        second_saved_news = saved_news[1]
        self.assertEqual(first_saved_news.title, 'Notícia de arquitetura')
        self.assertEqual(second_saved_news.title, 'Outra notícia de arquitetura')
