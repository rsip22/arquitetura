from django.http import HttpResponse


def home_page(req):
    return HttpResponse('<html><title>Novidades em arquitetura</title></html>')
