from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import StoryForm
from .models import Story, Tag
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def story(request):
    story_list = Story.objects.all()
    tag_list = Tag.objects.all()

    context = {
        "story_list": story_list,
        "tag_list": tag_list

    }
    return render(request, 'story/story.html', context)


def story_detail(request, slug=None):
    instance = get_object_or_404(Story, slug=slug)
    context = {
        "instance": instance
    }
    return render(request, 'story/story-detail.html', context)


def story_tag(request, name=None):
    story_list = Story.objects.filter(tag__name=name)
    tag_list = Tag.objects.all()

    context = {
        "story_list": story_list,
        "tag_list": tag_list,
        # "name": name
    }
    return render(request, 'story/tag-story.html', context)


@login_required(login_url='/admin/login/')
def story_create(request):
    form = StoryForm(request.POST or None, request.FILES or None)
    tag_list = Tag.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully created New Story.')
        else:
            messages.error(
                request, 'Error creating New Story. Please correct errors and Try again.')
    context = {
        "form": form,
        "tag_list": tag_list
    }
    return render(request, 'story/story-form.html', context)


# @login_required(login_url='/admin/login/')
# def story_update(request, id=None):
#     instance = get_object_or_404(Hero, id=id)
#     form = StoryForm(request.POST or None,
#                      request.FILES or None, instance=instance)
#     print(form)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             messages.success(
#                 request, 'You have successfully created New Story.')
#         else:
#             messages.error(
#                 request, 'Error creating New Story. Please correct errors and Try again.')
#     context = {
#         "instance": instance,
#         "form": form,
#         "update": True
#     }
#     return render(request, 'home/story-form.html', context)
