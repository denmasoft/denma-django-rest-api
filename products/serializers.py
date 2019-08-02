from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Product
        fields = ('name')