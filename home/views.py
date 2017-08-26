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
        filter_values = TimeoutOption.objects.filter(user_id=token.user_id, timeout=request.data['timeout']).all().last()
        if not filter_values:
            timeout = TimeoutOption(user_id=token.user_id, timeout=request.data['timeout'])
            timeout.save()
            return Response('success', status=status.HTTP_200_OK)
        return Response('it has been already set.', status=status.HTTP_200_OK)



