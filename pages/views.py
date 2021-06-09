from django.shortcuts import render


def index(request):
    """ Display homepage """
    template = "templates/pages/index.html"
    context = {
        # ADD STORIES DATA
    }
    return render(request, template, context)

