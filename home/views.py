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
import datetime
import json

import pymongo
from pymongo import MongoClient


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


class RetrieveDataViewFifteenMin(APIView):
    def get(self, request, format=None):
        data = []
        json_data = []
        mongoserver_uri = "mongodb://Readuser:jbh4S3pCpTGCdIGGVOU6@10.8.0.2:27017/admin"
        connection = MongoClient(host=mongoserver_uri)
        db = connection['cc_accounts']
        collection = db['LANDON_coinigy_account']
        latest_datatime = list(collection.find({}).sort('time', pymongo.DESCENDING).limit(1))[0]['time']
        for index in range(1, 31):
            diff_time = 15 * index
            curr_date_time = latest_datatime - datetime.timedelta(minutes=diff_time)
            end_time = curr_date_time - datetime.timedelta(minutes=0)
            start_time = curr_date_time - datetime.timedelta(minutes=5)
            # {'created': {'$lt': datetime.datetime.now(), '$gt': datetime.datetime.now() - timedelta(days=10)}}
            cursor_data_eachtime = collection.find({
                'time': {
                    '$gte': start_time,
                    '$lt': end_time
                }
            })
            data_eachtime = list(cursor_data_eachtime)
            data.append(data_eachtime)

        for idx, datums in enumerate(data):
            for datum in datums:
                json_data.append({'id': idx,
                                  'balance_curr_code': datum['balance_curr_code'],
                                  'balance_amount_avail': datum['balance_amount_avail'],
                                  'balance_amount_held': datum['balance_amount_held'],
                                  'balance_amount_total': datum['balance_amount_total'],
                                  'btc_balance': datum['btc_balance'],
                                  'last_price': datum['last_price'],
                                  'time': datum['time']})
        return Response(json_data, status=status.HTTP_200_OK)


class RetrieveDataViewFiveMin(APIView):
    def get(self, request, format=None):
        data = []
        json_data = []
        mongoserver_uri = "mongodb://Readuser:jbh4S3pCpTGCdIGGVOU6@10.8.0.2:27017/admin"
        connection = MongoClient(host=mongoserver_uri)
        db = connection['cc_accounts']
        collection = db['LANDON_coinigy_account']
        latest_datatime = list(collection.find({}).sort('time', pymongo.DESCENDING).limit(1))[0]['time']
        for index in range(1, 31):
            diff_time = 5 * index
            curr_date_time = latest_datatime - datetime.timedelta(minutes=diff_time)
            end_time = curr_date_time - datetime.timedelta(minutes=0)
            start_time = curr_date_time - datetime.timedelta(minutes=5)
            # {'created': {'$lt': datetime.datetime.now(), '$gt': datetime.datetime.now() - timedelta(days=10)}}
            cursor_data_eachtime = collection.find({
                'time': {
                    '$gte': start_time,
                    '$lt': end_time
                }
            })
            data_eachtime = list(cursor_data_eachtime)
            data.append(data_eachtime)

        for idx, datums in enumerate(data):
            for datum in datums:
                json_data.append({'id': idx,
                                  'balance_curr_code': datum['balance_curr_code'],
                                  'balance_amount_avail': datum['balance_amount_avail'],
                                  'balance_amount_held': datum['balance_amount_held'],
                                  'balance_amount_total': datum['balance_amount_total'],
                                  'btc_balance': datum['btc_balance'],
                                  'last_price': datum['last_price'],
                                  'time': datum['time']})
        return Response(json_data, status=status.HTTP_200_OK)


class RetrieveDataViewOneHour(APIView):
    def get(self, request, format=None):
        data = []
        json_data = []
        mongoserver_uri = "mongodb://Readuser:jbh4S3pCpTGCdIGGVOU6@10.8.0.2:27017/admin"
        connection = MongoClient(host=mongoserver_uri)
        db = connection['cc_accounts']
        collection = db['LANDON_coinigy_account']
        latest_datatime = list(collection.find({}).sort('time', pymongo.DESCENDING).limit(1))[0]['time']
        for index in range(1, 31):
            diff_time = 60 * index
            curr_date_time = latest_datatime - datetime.timedelta(minutes=diff_time)
            end_time = curr_date_time - datetime.timedelta(minutes=0)
            start_time = curr_date_time - datetime.timedelta(minutes=5)
            # {'created': {'$lt': datetime.datetime.now(), '$gt': datetime.datetime.now() - timedelta(days=10)}}
            cursor_data_eachtime = collection.find({
                'time': {
                    '$gte': start_time,
                    '$lt': end_time
                }
            })
            data_eachtime = list(cursor_data_eachtime)
            data.append(data_eachtime)

        for idx, datums in enumerate(data):
            for datum in datums:
                json_data.append({'id': idx,
                                  'balance_curr_code': datum['balance_curr_code'],
                                  'balance_amount_avail': datum['balance_amount_avail'],
                                  'balance_amount_held': datum['balance_amount_held'],
                                  'balance_amount_total': datum['balance_amount_total'],
                                  'btc_balance': datum['btc_balance'],
                                  'last_price': datum['last_price'],
                                  'time': datum['time']})
        return Response(json_data, status=status.HTTP_200_OK)


class RetrieveDataViewFourHours(APIView):
    def get(self, request, format=None):
        data = []
        json_data = []
        mongoserver_uri = "mongodb://Readuser:jbh4S3pCpTGCdIGGVOU6@10.8.0.2:27017/admin"
        connection = MongoClient(host=mongoserver_uri)
        db = connection['cc_accounts']
        collection = db['LANDON_coinigy_account']
        latest_datatime = list(collection.find({}).sort('time', pymongo.DESCENDING).limit(1))[0]['time']
        for index in range(1, 31):
            diff_time = 240 * index
            curr_date_time = latest_datatime - datetime.timedelta(minutes=diff_time)
            end_time = curr_date_time - datetime.timedelta(minutes=0)
            start_time = curr_date_time - datetime.timedelta(minutes=5)
            # {'created': {'$lt': datetime.datetime.now(), '$gt': datetime.datetime.now() - timedelta(days=10)}}
            cursor_data_eachtime = collection.find({
                'time': {
                    '$gte': start_time,
                    '$lt': end_time
                }
            })
            data_eachtime = list(cursor_data_eachtime)
            data.append(data_eachtime)

        for idx, datums in enumerate(data):
            for datum in datums:
                json_data.append({'id': idx,
                                  'balance_curr_code': datum['balance_curr_code'],
                                  'balance_amount_avail': datum['balance_amount_avail'],
                                  'balance_amount_held': datum['balance_amount_held'],
                                  'balance_amount_total': datum['balance_amount_total'],
                                  'btc_balance': datum['btc_balance'],
                                  'last_price': datum['last_price'],
                                  'time': datum['time']})
        return Response(json_data, status=status.HTTP_200_OK)


class RetrieveDataViewOneDay(APIView):
    def get(self, request, format=None):
        data = []
        json_data = []
        mongoserver_uri = "mongodb://Readuser:jbh4S3pCpTGCdIGGVOU6@10.8.0.2:27017/admin"
        connection = MongoClient(host=mongoserver_uri)
        db = connection['cc_accounts']
        collection = db['LANDON_coinigy_account']
        latest_datatime = list(collection.find({}).sort('time', pymongo.DESCENDING).limit(1))[0]['time']
        for index in range(1, 31):
            diff_time = index
            curr_date_time = latest_datatime - datetime.timedelta(days=diff_time)
            end_time = curr_date_time - datetime.timedelta(minutes=0)
            start_time = curr_date_time - datetime.timedelta(minutes=5)
            # {'created': {'$lt': datetime.datetime.now(), '$gt': datetime.datetime.now() - timedelta(days=10)}}
            cursor_data_eachtime = collection.find({
                'time': {
                    '$gte': start_time,
                    '$lt': end_time
                }
            })
            data_eachtime = list(cursor_data_eachtime)
            data.append(data_eachtime)

        for idx, datums in enumerate(data):
            for datum in datums:
                json_data.append({'id': idx,
                                  'balance_curr_code': datum['balance_curr_code'],
                                  'balance_amount_avail': datum['balance_amount_avail'],
                                  'balance_amount_held': datum['balance_amount_held'],
                                  'balance_amount_total': datum['balance_amount_total'],
                                  'btc_balance': datum['btc_balance'],
                                  'last_price': datum['last_price'],
                                  'time': datum['time']})
        return Response(json_data, status=status.HTTP_200_OK)


class RetrieveDataViewOneWeek(APIView):
    def get(self, request, format=None):
        data = []
        json_data = []
        mongoserver_uri = "mongodb://Readuser:jbh4S3pCpTGCdIGGVOU6@10.8.0.2:27017/admin"
        connection = MongoClient(host=mongoserver_uri)
        db = connection['cc_accounts']
        collection = db['LANDON_coinigy_account']
        latest_datatime = list(collection.find({}).sort('time', pymongo.DESCENDING).limit(1))[0]['time']
        for index in range(1, 31):
            diff_time = 7 * index
            curr_date_time = latest_datatime - datetime.timedelta(days=diff_time)
            end_time = curr_date_time - datetime.timedelta(minutes=0)
            start_time = curr_date_time - datetime.timedelta(minutes=5)
            # {'created': {'$lt': datetime.datetime.now(), '$gt': datetime.datetime.now() - timedelta(days=10)}}
            cursor_data_eachtime = collection.find({
                'time': {
                    '$gte': start_time,
                    '$lt': end_time
                }
            })
            data_eachtime = list(cursor_data_eachtime)
            data.append(data_eachtime)

        for idx, datums in enumerate(data):
            for datum in datums:
                json_data.append({'id': idx,
                                  'balance_curr_code': datum['balance_curr_code'],
                                  'balance_amount_avail': datum['balance_amount_avail'],
                                  'balance_amount_held': datum['balance_amount_held'],
                                  'balance_amount_total': datum['balance_amount_total'],
                                  'btc_balance': datum['btc_balance'],
                                  'last_price': datum['last_price'],
                                  'time': datum['time']})
        return Response(json_data, status=status.HTTP_200_OK)


class RetrieveLatestDataView(APIView):
    def get(self, request, format=None):
        json_data = []
        mongoserver_uri = "mongodb://Readuser:jbh4S3pCpTGCdIGGVOU6@10.8.0.2:27017/admin"
        connection = MongoClient(host=mongoserver_uri)
        db = connection['cc_accounts']
        collection = db['LANDON_coinigy_account']
        data = list(collection.find({}).sort('_id', pymongo.DESCENDING).limit(25))
        for datum in data:
            json_data.append({'id': str(datum['_id']),
                              'balance_curr_code': datum['balance_curr_code'],
                              'balance_amount_avail': datum['balance_amount_avail'],
                              'balance_amount_held': datum['balance_amount_held'],
                              'balance_amount_total': datum['balance_amount_total'],
                              'btc_balance': datum['btc_balance'],
                              'last_price': datum['last_price'],
                              'time': datum['time']})
        return Response(json_data, status=status.HTTP_200_OK)




















