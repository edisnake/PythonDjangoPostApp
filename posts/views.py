from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm

def index(request):
    """Query the 10 latest created post and list them."""

    # calling the latest 10 posts
    posts = Posts.objects.all().order_by('-created_ts')[:10]

    context = {
        'title': 'Latest Posts',
        'posts': posts
    }

    # Sending variables to the template
    return render(request, 'posts/index.html', context)

def details(request, post_id):
    """Get a given post and retrieve its info with read only access.
        Args:
           post_id (int): the post id to be queried.
    """
    post = Posts.objects.get(id=post_id)

    context = {
        'title': 'Post Info',
        'post': post
    }

    return render(request, 'posts/details.html', context)

def create(request):
    """Display a form to create a Post."""
    form = PostsForm(request.POST or None)

    # If the form is submited by user
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'title': 'Create Post',
        'form': form
    }

    return render(request, 'posts/post_form.html', context)

def update(request, post_id):
    """Get a given post and retrieve its info with modification access.
        Args:
           post_id (int): the post id to be updated.
    """
    post = Posts.objects.get(id=post_id)
    form = PostsForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'title': 'Update Post',
        'form': form,
        'post': post
    }

    return render(request, 'posts/post_form.html', context)

def delete(request, post_id):
    """Deletes a post asking for confirmation
        Args:
           post_id (int): the post id to be deleted.
    """
    post = Posts.objects.get(id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('index')

    context = {
        'title': 'Delete Post',
        'post': post
    }

    return render(request, 'posts/delete_confirm.html', context)
