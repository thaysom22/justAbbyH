from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.conf import settings

from .forms import StoryForm
from .models import Story
from .storage_helpers import create_presigned_url

import mimetypes  # ??


def stories(request):
    """ Display all stories in database on stories page """
    stories = Story.objects.all()  # retrieve all Story instances from database
    context = {
        'stories': stories,
    }
    template = "stories/stories.html"
    return render(request, template, context)


def story_detail(request, story_id):
    """ 
    Display detail about a particular story in database.
    Remove reference to pdf file from Story instance
    if user is not authenicated.
    """
    story = get_object_or_404(Story, pk=story_id)
    user_is_subscribed = False  # determine if download links will be in template
    if request.user.is_authenticated:
        user_is_subscribed = True
    else:
        # remove reference to pdf file from object passed to template (no change in database)
        story.pdf = None

    context = {
        'story': story,
        'user_is_subscribed': user_is_subscribed,
    }
    template = "stories/story_detail.html"
    return render(request, template, context)


@login_required
def add_story(request):
    """ 
    GET: Display add story form.
    POST: Add a story to the database.
    Access: staff only
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only the author can do that!')
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
    (staff only)
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only the author can do that!')
        return redirect(reverse('index'))
    
    story = get_object_or_404(Story, pk=story_id)
    if request.method == 'POST':
        edit_story_form = StoryForm(
            request.POST,
            request.FILES,
            instance=story)
        
        if edit_story_form.is_valid():
            edit_story_form.save()
            messages.success(request, 'Successfully updated story!')
            return redirect(reverse('story_detail', args=[story.id]))
        else:
            messages.error(request, 'Failed to update story - ensure form is valid.')

    else:
        # GET
        edit_story_form = StoryForm(instance=story)
        messages.info(request, f'You are editing {story.title}')
        
    context = {
        'edit_story_form': edit_story_form,
    }
    template = "stories/edit_story.html"
    return render(request, template, context)


@login_required
def delete_story(request, story_id):
    """ Delete a story in the database (staff only) """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only the author can do that!')
        return redirect(reverse('index'))
    
    story = get_object_or_404(Story, pk=story_id)
    story.delete()
    messages.success(request, 'Story was deleted.')
    return redirect(reverse('stories'))


@login_required
def download_story(request, story_id):
    """ Logged in user can access url for story pdf file """
    
    # get story instance from db by pk
    story = get_object_or_404(Story, pk=story_id)
    file_url = story.pdf.url
    filename = story.pdf.name

    if settings.USE_AWS:
        object_key = 'media/private/' + filename
        # generate presigned aws url
        presigned_url = create_presigned_url(
            settings.AWS_STORAGE_PRIVATE_BUCKET_NAME,
            object_key,
        )
        if presigned_url:
            # file in s3 bucket
            return redirect(presigned_url)
        else:
            return HttpResponseBadRequest(
                'Sorry - something went wrong. Please try again or \
                 contact me for assistance'
            )
    else:
        # file on local server
        return redirect(file_url)

    # CODE TO RETURN LOCAL FILE AS A DOWNLOAD - REMOVE? #  

    # filename = story.pdf.name.split('/')[-1]
    # # credit[1]
    # mime_type, _ = mimetypes.guess_type(file_url)  # guess type incase non-pdf file

    # print("mime type:", mime_type)

    # if not mime_type:
    #     mime_type = 'application/pdf'

    # fl = open(file_field, 'rb')  # read as binary (no encoding)
    # response = HttpResponse(fl, headers={
    #     'Content-Type': mime_type,
    #     'Content-Disposition': f"attachment; filename={filename}",
    # })
    # return response
