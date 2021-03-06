# -*- coding: utf-8 -*-
import datetime

# from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.


@python_2_unicode_compatible  # only if you need to support  python2
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def is_published_recently(self):
        now = timezone.now()
        return now > self.pub_date >= now - datetime.timedelta(days=1)
    is_published_recently.admin_order_field = 'pub_date'
    is_published_recently.boolean = True
    is_published_recently.short_description = 'Published recently?'


@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __str__(self):
        return self.choice_text
