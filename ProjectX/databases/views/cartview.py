from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from databases.models import Menu,Cart
from django.db.models import Subquery
from databases.serializers import MenuSerializer
from rest_framework.decorators import api_view, permission_classes
from ..serializers import CartSerializer

@api_view(['POST'])
def cartPost(request):
        print("here")
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET'])
def getCartItems(request, pk):
    data = Cart.objects.filter(User_Id=int(pk))
    data1 =Menu.objects.filter(id__in=Subquery(data.values('Food_Id')))

    serializer = CartSerializer(data, many=True)
    serializer1=MenuSerializer(data1,many=True)
    return Response( serializer1.data)