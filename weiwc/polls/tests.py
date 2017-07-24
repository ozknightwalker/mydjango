#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: weiwc
@license: Apache Licence 
@contact: 972237007@qq.com
@site: https://github.com/abelweiwencai
@software: PyCharm Community Edition
@file: tests.py
@time: 2017/7/15 14:19
"""

import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Question


class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is in future
        :return:
        """
        tmp_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=tmp_time)
        self.assertIs(future_question.is_published_recently(), False)
