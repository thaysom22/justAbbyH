from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required


def stories(request):
    """ Display all stories in database on stories page """

    context = {
        # ADD STORIES DATA HERE
    }
    template = "stories/stories.html"
    return render(request, template, context)


def story_detail(request, story_id):
    """ Display detail about a particular story in database """
    context = {
        # ADD STORY DATA HERE
    }
    template = "stories/story_detail.html"
    return render(request, template, context)


@login_required
def add_story(request):
    """ 
    GET: Display add story form
    POST: Add a story to the database
    """
    if request.method == "GET":
        context = {
            # ADD BLANK MODELFORM INSTANCE
        }
        template = "stories/add_story.html"
        return render(request, template, context)

    # POST

    # CREATE NEW MODEL INSTANCE FROM COMPLETED MODELFORM
    # SAVE MODEL TO DATEBASE
    return redirect(reverse('stories'))


@login_required
def edit_story(request, story_id):
    """ 
    GET: Display edit story form
    POST: Edit a story in the database
    """
    if request.method == "GET":
        # GET MODEL INSTANCE FROM DATABASE
        context = {
            # INSTANTIATE MODELFORM FROM MODEL INSTANCE
        }
        template = "stories/edit_story.html"
        return render(request, template, context)

    # POST

    # UPDATE MODEL INSTANCE USING MODELFORM
    # SAVE UPDATED MODEL TO DATABASE
    return redirect(reverse('stories'))


@login_required
def delete_story(request, story_id):
    """ Delete a story in the database """
    # DELETE MODEL INSTANCE FROM DATABASE
    return redirect(reverse('stories'))


@login_required
def download_story(request, story_id):
    """ Download a story pdf file """
    # RETURN PDF FILE DOWNLOAD IN NEW TAB?
    return None