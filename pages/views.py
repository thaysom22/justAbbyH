from django.shortcuts import render
from django.conf import settings


def index(request):
    """ Display homepage """
    template = "pages/index.html"
    context = {
        'page_title': 'Welcome',
    }
    return render(request, template, context)


def about(request):
    """ Display about page """
    template = "pages/about.html"
    context = {
        'page_title': 'About',
        'default_from_email': settings.DEFAULT_FROM_EMAIL,
    }

    return render(request, template, context)
    