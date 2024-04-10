from django.http import Http404
from django.shortcuts import render

from tests.conftest import EXPECTED_POSTS

posts = EXPECTED_POSTS


def index(request):
    template = 'blog/index.html'
    reversed_posts = posts[::-1]
    context = {'posts': reversed_posts}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    context = {}
    for post in posts:
        if post['id'] == id:
            context = {'post': post}
    if not context:
        raise Http404
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    for post in posts:
        post['category'] = category_slug
    context = {'post': post}
    return render(request, template, context)
