from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializers import *
# Create your views here.


class ReactView(APIView):
    serializer_class=ReactSerializer
    def get(self,request):
        
        output=[{"GST_no":output.GST_no,"Address":output.Addr,"Manager name":output.Mgr_name,"Manager number":output.Mgr_no,"Description":output.Descr} 
        for output in Restaurant.objects.all()]
        return Response(output)
    
    def post(self,request):
        serializer=ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)