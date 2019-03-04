# Arquitetura - web app em Django para notícias de arquitetura


Criar arquivo .env no diretório raiz do projeto com as seguintes variáveis:
```
LOGIN=
PASSWORD=
DJANGO_SETTINGS_MODULE=news.settings
SECRET_KEY=
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
