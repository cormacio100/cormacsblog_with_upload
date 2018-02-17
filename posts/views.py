# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

from .forms import BlogPostForm
from django.shortcuts import redirect

import logging
logger = logging.getLogger(__name__)



def index(request):
    return render(request, 'posts/index.html')


def home(request):
    #   retrieve all posts and REVEERSE ORDDERED by date
    posts = Post.objects.order_by('-published_date')
    args = {'posts': posts}
    return render(request, 'posts/home.html', args)


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    args = {'posts': posts}
    return render(request, 'posts/post_listing.html', args)


def post_details(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    #post = Post.objects.get(pk=post_id)
    return render(request, 'posts/post_details.html', {'post': post})


def new_post(request):
    """
    If the view was accessed because the Submit button was clicked, then it
    will be true that the request.method == POST
    """
    if request.method=="POST":
        logger.debug('contents of request.FILES is ')
        logger.debug(request.FILES)
        #logger.debug('contents of request.body is ')
        #logger.debug( request.body)

        #   retrieve the values from teh submitted form
        form = BlogPostForm(request.POST, request.FILES)
        #   check if valid
        if form.is_valid():
            #   stop the form from saving to DB just yet
            #   but save it as an instance of Post model
            #   Hold off on saving until extra values have been added to the Post model (LOGIC HOOK)
            post = form.save(commit=False)
            #   then retrieve values to add to the model
            post.author = request.user  #   must be logged in (even in admin) for this value to exist
            post.published_date = timezone.now()
            #   save to the model
            post.save()
            #   Redirect user to post_details
            logger.debug('post.pk is ')
            logger.debug(post.pk)
            #return redirect(post_details,post.pk)
            return HttpResponse('post uploaded')
    else:
        form = BlogPostForm()
    return render(request,'posts/blog_posts_form.html',{'form':form})

