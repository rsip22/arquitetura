import time
import unittest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver


class NovoArquitetoTeste(unittest.TestCase):
    """
    Dado que sou um Arquiteto eu posso visualizar notícias, então poderei
    ficar informado sobre as novidades em arquitetura.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_pode_acessar_home_e_encontrar_o_site(self):
        """ Arquiteto acessa a Home do site """
        self.selenium.get('http://localhost:8000')
        self.assertIn('Novidades em arquitetura', self.selenium.title)

    def test_pode_ver_noticias_de_arquitetura_com_titulo_e_imagem(self):
        """
        Arquiteto acessa a Home do site, consegue visualizar as notícias
        mais recentes sobre arquitetura, com uma imagem de capa e título
        """
        self.selenium.get('http://localhost:8000')

        section_news = self.selenium.find_element_by_tag_name('section')

        news_item = section_news.find_elements_by_tag_name('article')
        self.assertTrue(
            any(
                item.text == 'Notícia de arquitetura'
                for item in news_item
            )
        )

        news_img = section_news.find_elements_by_tag_name('img')
        self.assertTrue(
            any(
                'dummy.png' in image.get_attribute('src')
                for image in news_img
            )
        )

    def test_arquiteto_seleciona_noticia_visualiza_conteudo(self):
        """
        Arquiteto na Home do site, seleciona uma notícia de
        interesse para visualizar o conteúdo na íntegra.
        """
        self.selenium.get('http://localhost:8000')
        section_news = self.selenium.find_element_by_tag_name('section')
        list_news = section_news.find_element_by_tag_name('a')
        list_news.send_keys(Keys.ENTER)
        time.sleep(1)

        news_article = self.selenium.find_element_by_tag_name('article')
        news_title = news_article.find_element_by_tag_name('h2')
        news_image = news_article.find_elements_by_tag_name('img')
        news_text = news_article.find_elements_by_tag_name('p')

        self.assertIn('Notícia de arquitetura', news_title.text)

        self.assertTrue(
            any(
                'dummy.png' in image.get_attribute('src')
                for image in news_image
            )
        )

        self.assertTrue(
            any(
                '<p>Exemplo de notícia de arquitetura</p>' in text.text
                for text in news_text
            )
        )

    # =======
    # Dado que sou um Arquiteto eu posso visualizar uma notícia na íntegra
    # então poderei ver todo o seu conteúdo.

    # Arquiteto pode visualizar uma imagem de capa da notícia
    # e o conteúdo da mesma

    # =======
    # Dado que sou um Arquiteto eu posso visualizar as notícias filtradas por
    # suas categorias então eu poderei selecionar as notícias de meu interesse.

    # Arquiteto na Home do site, informa a categoria que deseja e assim
    # as notícias relacionadas àquela categoria são exibidas

    def test_unfinished_tests(self):
        self.fail('Finish the test!')

# =======
# Dado que sou um Administrador eu posso acessar uma área restrita e segura
# para que somente eu possa inserir novas notícias.

# Administrador pode informar o e-mail e senha para acessar a plataforma.

# =======
# Dado que sou um Administrador eu posso inserir novas notícias no website
# então os Arquitetos possam consumir o conteúdo.

# Administrador consegue definir uma imagem de capa e o texto da notícia.

# Administrador consegue informar a qual categoria a notícia pertence.


if __name__ == '__main__':
    unittest.main()
