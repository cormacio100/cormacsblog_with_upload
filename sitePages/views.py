# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def about(request):
    return render(request, 'sitePages/about.html')


def index(request):
    return render(request, 'posts/index.html')