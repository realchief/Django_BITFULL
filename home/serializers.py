from django.contrib.auth.models import User, Group
from rest_framework import serializers
from home.models import TimeoutOption


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TimeoutOptionSerializer(serializers.Serializer):
    class Meta:
        model = TimeoutOption
        fields = ('token', 'timeout')
        token = serializers.CharField(max_length=200)
        timeout = serializers.IntegerField()

