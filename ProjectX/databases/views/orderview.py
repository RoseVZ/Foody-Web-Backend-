from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from databases.models import Cart
from databases.serializers import MenuSerializer,OrderSerializer
from rest_framework.decorators import api_view, permission_classes

@api_view(['POST'])
def saveOrder(request):
        print("here")
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)