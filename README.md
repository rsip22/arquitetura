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
