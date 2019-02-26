from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase

from news.views import home_page


class HomePageTest(TestCase):

    def test_pagina_raiz_resolve_para_view_da_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_pagina_raiz_retona_html_correto(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Novidades em arquitetura</title>', html)
        self.assertTrue(html.endswith('</html>'))
