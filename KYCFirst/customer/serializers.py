from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Customer
        fields = '__all__'