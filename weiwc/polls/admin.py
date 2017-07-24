# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice

# Register your models here



# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('This is title', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'is_published_recently')
    list_filter = ['question_text', 'pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

