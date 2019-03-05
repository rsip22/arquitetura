import environ
import time
import unittest

from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver

from news.models import AdminUser, Tag

# Load environment variables
env = environ.Env(
        DEBUG=(bool, True),
    )
environ.Env.read_env(settings.PROJECT_ENV)

# Time for Selenium to wait, in seconds
MAX_WAIT = 1


class NovoArquitetoTeste(StaticLiveServerTestCase):
    """
    Dado que sou um Arquiteto eu posso visualizar notícias, então poderei
    ficar informado sobre as novidades em arquitetura.
    """

    fixtures = ['news/fixtures/news.json']

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
        self.selenium.get(self.live_server_url)
        self.assertIn('Novidades em arquitetura', self.selenium.title)

    def test_pode_ver_noticias_com_titulo_imagem_e_tags(self):
        """
        Arquiteto acessa a Home do site, consegue visualizar as notícias
        mais recentes sobre arquitetura, com uma imagem de capa e título
        """
        self.selenium.get(self.live_server_url)

        section_news = self.selenium.find_element_by_tag_name('section')
        news_title = section_news.find_elements_by_tag_name('h2')
        news_img = section_news.find_elements_by_tag_name('img')

        self.assertTrue(
            any(
                item.text == 'Notícia de arquitetura'
                for item in news_title
            )
        )

        self.assertTrue(
            any(
                '/media/media/139.jpg' in image.get_attribute('src')
                for image in news_img
            )
        )

    def test_arquiteto_seleciona_noticia_visualiza_integra_conteudo(self):
        """
        Arquiteto na Home do site, seleciona uma notícia de
        interesse para visualizar o conteúdo na íntegra.
        """
        self.selenium.get(self.live_server_url)
        section_news = self.selenium.find_element_by_tag_name('section')
        list_news = section_news.find_element_by_tag_name('a')
        list_news.send_keys(Keys.ENTER)

        # Wait for new page to load
        while True:
            try:
                news_article = self.selenium.find_element_by_tag_name('main')
                news_title = news_article.find_element_by_tag_name('h1')
                news_image = news_article.find_elements_by_tag_name('img')
                news_text = news_article.find_elements_by_tag_name('p')
                news_tags = news_article.find_elements_by_tag_name('li')
                break
            except NoSuchElementException:
                time.sleep(MAX_WAIT)

        self.assertIn('Notícia de arquitetura', news_title.text)

        """
        Sendo um Arquiteto eu posso visualizar uma imagem de capa de notícia
        e o conteúdo da mesma.
        """
        self.assertTrue(
            any(
                '/media/media/139.jpg' in image.get_attribute('src')
                for image in news_image
            )
        )

        self.assertTrue(
            any(
                'Lorem ipsum dolor sit amet,'
                + ' consectetur adipiscing elit.' in text.text
                for text in news_text
            )
        )

        """
        Arquiteto pode visualizar as notícias filtradas por suas categorias
        e eu pode selecionar as notícias de seu interesse.
        """
        self.assertTrue(
            any(
                'arquitetura' in tags.text
                for tags in news_tags
            )
        )

    def test_arquiteto_seleciona_noticias_por_tag(self):
        """
        Arquiteto na Home do site, informa a categoria que deseja e assim
        as notícias relacionadas àquela categoria são exibidas
        """

        self.selenium.get(self.live_server_url)
        news_tag = self.selenium.find_element_by_tag_name('li')
        tag_link = news_tag.find_element_by_tag_name('a')
        tag_link.send_keys(Keys.ENTER)

        # Wait for new page to load
        while True:
            try:
                item_tags = self.selenium.find_elements_by_tag_name('li')
                break
            except NoSuchElementException:
                time.sleep(MAX_WAIT)

        self.assertTrue(
            any(
                'arquitetura' in tags.text
                for tags in item_tags
            )
        )


class AdministradorTeste(StaticLiveServerTestCase):
    """
    Dado que sou um Administrador eu posso acessar uma área restrita e segura
    para que somente eu possa inserir novas notícias.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        self.user = AdminUser.objects.create_superuser(
            username=env('LOGIN'),
            email=env('EMAIL'),
            password=env('PASSWORD'))
        self.tags = Tag.objects.create(name='arquitetura')

    def test_administrador_pode_acessar_area_restrita_com_email_e_senha(self):
        """
        Administrador pode informar o e-mail e senha para acessar a plataforma.
        OBS: Em produção, usuário, email e senha devem ter sido cadastrados
        anteriormente, através do createsuperuser.
        """
        self.selenium.get(f'{self.live_server_url}/admin')

        try:
            input = self.selenium.find_element_by_id('id_username')
            input.send_keys(env('EMAIL'))
            input = self.selenium.find_element_by_id('id_password')
            input.send_keys(env('PASSWORD'))
            input.send_keys(Keys.ENTER)
        except Exception as e:
            print(e)

    def test_administrador_pode_inserir_novas_noticas_no_site(self):
        """
        Administrador pode inserir novas notícias no website
        """
        self.selenium.get(f'{self.live_server_url}/admin')

        try:
            input = self.selenium.find_element_by_id('id_username')
            input.send_keys(env('EMAIL'))
            input = self.selenium.find_element_by_id('id_password')
            input.send_keys(env('PASSWORD'))
            input.send_keys(Keys.ENTER)
        except Exception as e:
            print(e)

        # Wait for new page to load
        while True:
            try:
                model_post = self.selenium.find_element_by_class_name(
                    'model-post')
                link_add = model_post.find_element_by_link_text('Add')
                break
            except NoSuchElementException:
                time.sleep(MAX_WAIT)

        link_add.click()

        time.sleep(MAX_WAIT)

        try:
            input = self.selenium.find_element_by_id('id_title')
            input.send_keys('Test title for post')

            # Administrador consegue definir o texto da notícia.
            input = self.selenium.find_element_by_id('id_text')
            input.send_keys('Lorem ipsum dolor simet')

            # Administrador consegue definir uma imagem de capa
            input = self.selenium.find_element_by_id(
                        'id_image_path').send_keys(
                        f'{settings.MEDIA_DIR}{settings.MEDIA_URL}/139.jpg')

            # Administrador consegue tornar pública a notícia
            publish = self.selenium.find_element_by_class_name(
                        'field-published_date')
            pub_date = publish.find_element_by_link_text('Today')
            pub_date.click()
            pub_time = publish.find_element_by_link_text('Now')
            pub_time.click()

            # Administrador consegue informar a qual categoria
            # a notícia pertence.
            try:
                self.selenium.find_element_by_xpath(
                    '//select[@id="id_tags"]'
                    + '/option[text()="arquitetura"]').click()
            except Exception as e:
                print(e)

            submit_row = self.selenium.find_element_by_class_name('submit-row')
            input = submit_row.find_element_by_class_name(
                    'default').send_keys(Keys.ENTER)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
