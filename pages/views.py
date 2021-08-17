from django.shortcuts import render


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
    }
    return render(request, template, context)
    