# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import datetime
# Create your models here.
from django.db import models
from django.utils import timezone


@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text



@python_2_unicode_compatible
class Order(models.Model):
    order_number = models.CharField(max_length=200)
    orderable_name = models.CharField(max_length=200)
    orderable_code = models.CharField(max_length=200)
    patient_id = models.IntegerField(default=0)
    rpl_name = models.CharField(max_length=200)
    rpl_code = models.CharField(max_length=200)
    ordered_by = models.CharField(max_length=200)
    supervised_by = models.CharField(max_length=200)
    managed_by = models.CharField(max_length=200)
    problem_ids = models.CharField(max_length=200)
    req_number = models.CharField(max_length=200)
    order_item_id = models.CharField(max_length=200)


    def __str__(self):
        return self.choice_text