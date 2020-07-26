from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Post, Author, Comment
from .forms import CreatePostForm, CommentForm


def create_post(request):
    forms = CreatePostForm()
    context = {
        'forms': forms
    }
    return render(request, 'blog/create_post.html', context)


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/author_list.html', {'authors': authors})


def authors_post(request, author_name):
    author = Author.objects.get(name=author_name)
    posts = Post.objects.filter(author=author)
    return render(request, 'blog/authors_post.html', {'posts': posts, 'name': author_name})


def post_list(request):
    posts = Post.objects.all()
    context = {
        'post_list': posts
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'blog/post_detail.html', context)