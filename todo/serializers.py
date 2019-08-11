#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2019 Roman <namor925@gmail.com>
#

from rest_framework import serializers
from .models import Tasks

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('title',  'target_user', 'status', 'date_create')

    def create_task(self):
        pass
