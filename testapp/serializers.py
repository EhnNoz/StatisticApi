from rest_framework import serializers
import pytz
from django.utils import timezone
from .models import *



    
class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = ['id', 'name', 'url','admin_tel','admin_email','token']
        
        

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'system', 'user_id','ip','user_agent','referer','xReferer','start_time','End_time']