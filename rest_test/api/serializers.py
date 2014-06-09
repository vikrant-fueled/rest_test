# -*- coding: utf-8 -*-

from rest_framework import serializers

from users.models import User
from core.models import Selfie, Like

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'email')
        read_only_fields = ()


class SelfieSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Selfie
        fields = ('id', 'user', 'caption', 'category', 'imageSize', 'imageUrl', 'isDeleted')
        read_only_fields = ()
