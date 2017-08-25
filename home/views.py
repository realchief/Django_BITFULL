# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from home.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from home.serializers import TimeoutOptionSerializer

from .models import TimeoutOption


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
    def get(self, request, format=None):
        timeoutoptions = TimeoutOption.objects.all()
        serializer = TimeoutOptionSerializer(timeoutoptions, many=True)
        return Response(serializer.data)
        # pass

    def post(self, request, format=None):
        serializer = TimeoutOptionSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # pass

    def put(self, request, token, format=None):
        timeoutoption = self.get_object(token)
        serializer = UserSerializer(timeoutoption, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # pass

    def delete(self, request, token, format=None):
        timeoutoption = self.get_object(token)
        timeoutoption.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
