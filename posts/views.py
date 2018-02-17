# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.


def index(request):
    return render(request, 'posts/index.html')


def home(request):
    #   retrieve all posts and REVEERSE ORDDERED by date
    posts = Post.objects.order_by('-pub_date')
    args = {'posts': posts}
    return render(request, 'posts/home.html', args)

def post_list(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    args = {'posts': posts}
    return render(request, 'posts/post_listing.html', args)


def post_details(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    #post = Post.objects.get(pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})