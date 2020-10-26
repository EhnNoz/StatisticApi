from rest_framework import serializers
from .models import *



    
class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = ['id', 'name', 'url','admin_tel','admin_email','token']
        
        

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'system', 'user_id','ip','user_agent','referer','xReferer','start_time','End_time']
        


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'session', 'channel_id','content_id','content_type_id','service_id','action_id','time_code']