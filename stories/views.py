from django.shortcuts import render


def stories(request):
    """ Displays all stories in database on stories page """

    context = {
        # ADD STORIES DATA HERE
    }
    template = "stories/stories.html"
    return render(request, template)