import unittest

from selenium.webdriver.firefox.webdriver import WebDriver


class NovoArquitetoTeste(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    # =======
    # Dado que sou um Arquiteto eu posso visualizar notícias, então poderei
    # ficar informado sobre as novidades em arquitetura.

    # Arquiteto acessa a Home do site
    def test_pode_acessar_home_e_encontrar_o_site(self):
        self.selenium.get('http://localhost:8000')
        self.assertIn('Novidades em arquitetura', self.selenium.title)

    # Arquiteto acessa a Home do site, consegue visualizar as notícias
    # mais recentes sobre arquitetura, com uma imagem de capa e título
    def test_pode_ver_noticias_de_arquitetura(self):
        self.selenium.get('http://localhost:8000')
        section_news = self.selenium.find_element_by_tag_name('section')
        news_item = section_news.find_elements.by_tag_name('article')
        self.assertTrue(news_item.h1 == '' for item in news_item)

    # =======
    # Dado que sou um Arquiteto eu posso visualizar uma notícia na íntegra
    # então poderei ver todo o seu conteúdo.

    # Arquiteto na Home do site, seleciona uma notícia de
    # interesse para visualizar o conteúdo na íntegra.

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
