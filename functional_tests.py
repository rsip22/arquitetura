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
    def test_pode_ver_noticias_de_arquitetura(self):
        self.selenium.get('http://localhost:8000')
        self.assertIn('Novidades em arquitetura', self.selenium.title)
        self.fail('Finish the test!')

    # Arquiteto acessa a Home do site, consegue visualizar as notícias
    # mais recentes sobre arquitetura, com uma imagem de capa e título

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
