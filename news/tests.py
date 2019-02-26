from django.urls import resolve
from django.test import TestCase
from news.views import home_page


class HomePageTest(TestCase):

    def test_pagina_raiz_resolve_para_view_da_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)