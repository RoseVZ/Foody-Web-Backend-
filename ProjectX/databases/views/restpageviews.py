from django.db.models import Subquery
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from databases.models import Menu,Restaurant,OrderItems
from databases.serializers import MenuSerializer,RestaurantSerializer,OrderItemsSerializer,Food_OrderSerializer
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
def getRestID(request, pk):
    data = Restaurant.objects.all().filter(User_Id=int(pk))
    serializer = RestaurantSerializer(data, many=True)
    return Response( serializer.data)

@api_view(['GET'])
def getRestItems(request, pk):
    data = Menu.objects.filter(GST_no=int(pk))
    data1 =OrderItems.objects.filter(Food_Id__in=Subquery(data.values('id'))).distinct('Order_Id')
    
    serializer = MenuSerializer(data, many=True)
    serializer1=OrderItemsSerializer(data1,many=True)
    serializer2=Food_OrderSerializer(data1,many=True)
    return Response( serializer1.data)


@api_view(['GET'])
def getRestItems1(request, pk):
    data = Menu.objects.filter(GST_no=int(pk))
    data1 =OrderItems.objects.filter(Food_Id__in=Subquery(data.values('id')))
    data2 = Menu.objects.filter(id__in=Subquery(data1.values('Food_Id')))
    serializer = MenuSerializer(data2, many=True)
    # serializer1=OrderItemsSerializer(data1,many=True)
    # serializer2=Food_OrderSerializer(data1,many=True)
    return Response( serializer.data)
