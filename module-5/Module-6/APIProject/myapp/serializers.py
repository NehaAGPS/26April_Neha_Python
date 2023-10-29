from rest_framework import serializers
from .models import *

class userSerializers(serializers.ModelSerializer):
    class Meta:
        model=userinfo
        fields='__all__'