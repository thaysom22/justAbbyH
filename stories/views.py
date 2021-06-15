from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import StoryForm
from .models import Story


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
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can do that.')
        return redirect(reverse('index'))

    if request.method == "GET":
        add_story_form = StoryForm()
        context = {
            'add_story_form': add_story_form,
        }
        template = "stories/add_story.html"
        return render(request, template, context)

    # POST 
    add_story_form = StoryForm(
        request.POST,
        request.FILES
    )
    if add_story_form.is_valid():
        story = add_story_form.save() 
        messages.success(request, 'Successfully added story!')
        return redirect(reverse('story_detail', args=[story.id]))
    else:
        messages.error(request, add_story_form.errors)
        return redirect(reverse('add_story'))


@login_required
def edit_story(request, story_id):
    """ 
    GET: Find story and populate edit story form 
    POST: Edit a story in the database
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can do that.')
        return redirect(reverse('index'))
    
    # try to find story in database by story_id url parameter
    story = get_object_or_404(Story, pk=story_id)

    if request.method == "GET":
        edit_story_form = StoryForm(instance=story)
        messages.info(request, f'You are editing {story.title}')
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