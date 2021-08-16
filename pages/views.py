from django.shortcuts import render
from django.contrib import messages

def index(request):
    """ Display homepage """
    template = "pages/index.html"

    # TEST
    messages.debug(request, 'SQL statements were executed.')
    messages.info(request, 'Three credits remain in your account.')
    messages.success(request, 'Profile details updated.')
    messages.warning(request, 'Your account expires in three days.')
    messages.error(request, 'Document deleted.')

    return render(request, template)


def about(request):
    """ Display about page """
    template = "pages/about.html"
    return render(request, template)

