#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2019 Roman <namor925@gmail.com>
#

from rest_framework import serializers
from .models import Tasks
#from api.models import User #,  UserProfile
'''
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}
        

'''
class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('title',  'target_user', 'status', 'date_create', 'prioritet')

    def create_task(self):
        pass
