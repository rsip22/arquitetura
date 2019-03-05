# Arquitetura - web app em Django para notícias de arquitetura

## Para rodar o projeto:

1. Criar virtualenv:
```
$ python3 -m venv myvenv
```

2. Instalar dependências
```
$ pip install -r requirements.txt
```

3. Criar arquivo .env no diretório raiz do projeto com as seguintes variáveis:
```
LOGIN=
EMAIL=
PASSWORD=
SECRET_KEY=
```

4. Para criar superusuário e utilizar a interface administrativa:
```
(myvenv)$ python manage.py createsuperuser
```

5. Para rodar o servidor de desenvolvimento:
```
(myvenv)$ python manage.py runserver 0.0.0.0:8000
```

## Testando a aplicação:

Você vai precisar ter o Geckodriver instalado e disponível no PATH para utilizar o Selenium.

- Baixe o geckodriver:
[https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)

- OU com wget:
```
$ wget -cv https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
```

- Extraia, mova para o diretório bin e coloque no PATH:
```
$ tar -xvzf geckodriver-v0.24.0-linux64.tar.gz
$ sudo cp geckodriver /usr/local/bin
$ sudo chmod +x /usr/local/bin/geckodriver
$ export PATH=$PATH:/usr/local/bin/geckodriver
```

- Rodar testes funcionais:
```
(myvenv)$ python manage.py test functional_tests
```

- Rodar testes unitários:
```
(myvenv)$ python manage.py test news
```

### Cobertura dos testes:
```
Name                                         Stmts   Miss  Cover
----------------------------------------------------------------
news/__init__.py                                 0      0   100%
news/admin.py                                   46     46     0%
news/migrations/0001_initial.py                  6      0   100%
news/migrations/0002_auto_20190304_2010.py       4      0   100%
news/migrations/__init__.py                      0      0   100%
news/models.py                                  53     35    34%
news/urls.py                                     4      0   100%
news/views.py                                   13      0   100%
----------------------------------------------------------------
TOTAL                                          126     81    36%
```

## Estrutura do projeto:
```
.
├── README.md
├── functional_tests
│   └── tests.py
├── manage.py
├── media
│   └── media
│       ├── 139.jpg
│       └── 287.jpg
├── news                            # Aplicação de notícias
│   ├── __init__.py
│   ├── admin.py                    # Config administração
│   ├── apps.py                     # Config app
│   ├── fixtures
│   │   └── news.json               # Fixtures para testes
│   ├── migrations
│   ├── models.py                   # Modelos para o banco de dados
│   ├── static
│   ├── templates                   # Templates da app
│   │   ├── base.html               # Template base
│   │   ├── categories_list.html    # Template para a lista por categoria
│   │   ├── home.html               # Template da página inicial
│   │   └── post_detail.html        # Template detalhe do post
│   ├── tests.py                    # Testes unitários app
│   ├── urls.py                     # Configuração de roteamento da app
│   └── views.py                    # Configuração das views
├── requirements.txt
└── website
    ├── __init__.py
    ├── auth_backend.py             # Autenticação administrador
    ├── settings.py                 # Configurações do projeto
    ├── urls.py                     # Roteamento do projeto
    └── wsgi.py
```
