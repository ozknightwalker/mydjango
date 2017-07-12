# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from . import models

from django.template import loader

# Create your views here.

def index(request):
    latest_question_list = models.Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    try:
        question = models.Question.objects.get(pk=question_id)
    except models.Question.DoesNotExist:
        raise Http404("Question does not exist")
    # return HttpResponse(u"you are looking at {rid}".format(rid=question_id))
    return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
    return HttpResponse(u"you are looking at the results of {rid}!".format(rid=question_id))


def vote(request, question_id):
    return HttpResponse(u"you are voting on {rid}".format(rid=question_id))
