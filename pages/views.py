from django.shortcuts import render


def index(request):
    """ Display homepage """
    template = "pages/index.html"
    return render(request, template)


def about(request):
    """ Display about page """
    template = "pages/about.html"
    return render(request, template)

