from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializers import *
# Create your views here.


class ReactView(APIView):
    serializer_class=ReactSerializer
    def get(self,request):
        
        output=[{"GST":output.GST_no,"Address":output.Addr,"Mananger_no":output.Mgr_no,"Manager_name":output.Mgr_name,"Description":output.Descr} 
        for output in Restaurant.objects.all()]
        return Response(output)
    
    def post(self,request):
        serializer=ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)