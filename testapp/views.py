from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
#from testapp.serializers import NameSerializer
from testapp.serializers import SessionSerializer
#import time

#import pika
#import json
#from testapp.models import CR_TABLE
from testapp.models import Session
from testapp.models import System

#credentials = pika.PlainCredentials(username='admin', password='admin')
#connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.143.17',port=5672,credentials=credentials))

class TestAPIView(APIView):

    
    
    def post(self, request, *args, **kwargs):

        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            
            system = serializer.data.get('system')
            user_id = serializer.data.get('user_id')
            ip = serializer.data.get('ip')
            user_agent = serializer.data.get('user_agent')
            referer = serializer.data.get('referer')
            a=[]
            a=referer.split("?token=")
            eurl=a[0]
            etoken=a[1]
            print(a)
            start = time.time()
            print(start)
            xReferer = serializer.data.get('xReferer')
            End_time = serializer.data.get('End_time')
#            time = serializer.data.get('created_at')
#            a=Session.referer
#            print(a)
#            url = serializer2.data('url')
            if System.objects.filter(token=etoken).filter(url__contains=eurl).exists():
                Session.objects.create(system=system,user_id=user_id,ip=ip,user_agent=user_agent,referer=referer,xReferer=xReferer)
                return Response(status=200)

            else:

                return Response(status=403)
#2020-10-21 10:26:26.303984        
    
#    def patch(self, request, *args, **kwargs):
#        
#         
#        serializer = SessionSerializer(data=request.data)
#        if serializer.is_valid():
#            system = serializer.data.get('system')
#            user_id = serializer.data.get('user_id')
#            ip = serializer.data.get('ip')
#            user_agent = serializer.data.get('user_agent')
#            referer = serializer.data.get('referer')
#            a=[]
#            a=referer.split("?token=")
#            eurl=a[0]
#            etoken=a[1]
#            print(a)
#            start = time.time()
#            print(start)
#            xReferer = serializer.data.get('xReferer')
#            End_time = serializer.data.get('End_time')
##            xReferer = serializer.data.get('xReferer')
#            if Session.objects.filter(user_id=user_id):
#                 Session.objects.filter(user_id=user_id).update(system=system,user_id=user_id,ip=ip,user_agent=user_agent,referer=referer,xReferer='201')
#                 return Response(status=201)

#            




    
        





  

