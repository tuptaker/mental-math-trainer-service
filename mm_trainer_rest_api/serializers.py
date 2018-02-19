from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.utils import timezone
from rest_framework.authtoken.models import Token

class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ('key', 'user')