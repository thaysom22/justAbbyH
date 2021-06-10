from django.shortcuts import render


def index(request):
    """ Display homepage """
    template = "pages/index.html"
    context = {
        # ADD STORIES DATA
    }
    return render(request, template, context)


def about(request):
    """ Display about page """
    template = "pages/about.html"
    return render(request, template)

