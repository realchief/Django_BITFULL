# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from home.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from home.serializers import UserSerializer
from .models import TimeoutOption
from rest_framework.parsers import FormParser
from rest_framework.authtoken.models import Token

import pymongo
from pymongo import MongoClient


MONGO_HOST = "10.8.0.2"
MONGO_DB = "cc_accounts"
MONGO_USER = "Readuser"
MONGO_PASS = "jbh4S3pCpTGCdIGGVOU6"

mongoserver_uri = "mongodb://Readuser:jbh4S3pCpTGCdIGGVOU6@10.8.0.2:27017/admin"
conection = MongoClient(host=mongoserver_uri)
db = conection['cc_accounts']
collection = db['LANDON_coinigy_account']
a = collection.find_one()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TimeoutOptionView(APIView):
    parser_classes = (FormParser,)

    def post(self, request, format=None):
        token = Token.objects.get(key=request.auth)
        curr_user_id = token.user_id
        curr_timeout = request.data['timeout']
        if TimeoutOption.objects.all():
            if TimeoutOption.objects.get(user_id=token.user_id):
                timeout = TimeoutOption.objects.get(user_id=token.user_id)
                timeout.timeout = curr_timeout
            else:
                timeout = TimeoutOption(user_id=curr_user_id, timeout=curr_timeout)
        else:
            timeout = TimeoutOption(user_id=curr_user_id, timeout=curr_timeout)

        timeout.save()
        return Response('success', status=status.HTTP_200_OK)
















