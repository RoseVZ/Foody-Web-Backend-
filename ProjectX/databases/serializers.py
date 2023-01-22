from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField 
from django.contrib.auth import get_user_model
from .models import *
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name','password')
class RestaurantSerializer(serializers.ModelSerializer):
   
    class Meta:
        model= Restaurant
        fields='__all__'

class MenuSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Menu
        fields='__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields="__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =Order
        fields="__all__"