from rest_framework import serializers
from .models import Cities,States

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['city_name','city_id']



class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ['state_name','state_id']
         