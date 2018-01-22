# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# title, date, picture, text
class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="media/")       # need to install Pillow to use
    body = models.TextField()

    # make title visible in admin instead of Post Object
    def __unicode__(self):
        return self.title

    #   make the pub_date more readable by providing a format
    #   can be called directly from the template
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %d %Y')

    def summary(self):
        return self.body[:100]