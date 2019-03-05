# Arquitetura - web app em Django para notícias de arquitetura


Criar arquivo .env no diretório raiz do projeto com as seguintes variáveis:
```
LOGIN=
EMAIL=
PASSWORD=
SECRET_KEY=
```

Criar superusuário com username, login e senha do arquivo .env:

```
(myvenv)$ python manage.py createsuperuser
```

## Para rodar os testes:

Testes funcionais:

```
(myvenv)$ python manage.py test functional_tests
```

Testes unitários:

```
(myvenv)$ python manage.py test news
```

Cobertura dos testes:
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

Estrutura:

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
