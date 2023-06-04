from rest_framework import serializers
from .models import *


class AlcogolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alcogol
        fields = '__all__'