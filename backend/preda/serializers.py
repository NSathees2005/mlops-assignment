from rest_framework import serializers
from .models import React

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['v1', 'v2', 'v3', 'v4', 'v5']