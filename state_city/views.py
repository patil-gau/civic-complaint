from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CitySerializer,StateSerializer
from django.http import HttpResponseBadRequest
from .models import Cities,States
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
@api_view(['POST'])
def AddCity(request):
    if request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"New City added Successfully"})
    
    return HttpResponseBadRequest

@api_view(['POST'])
def AddState(request):
    if request.method == 'POST':
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"New State added Successfully"})
        else:
            return Response({"Message":"something went wrong"})    
    
    return HttpResponseBadRequest
    

@api_view(['GET'])
def DisplayCities(request,pk):
    if request.method == 'GET':
        all_citites = Cities.objects.filter(state_id=pk)
        print(all_citites)
        serializer = CitySerializer(all_citites,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')


@api_view(['GET'])
def DisplayStates(request):
     if request.method == 'GET':
        all_states = States.objects.all()
        print(all_states)
        serializer = StateSerializer(all_states,many=True)
        print(serializer)
        json_data = JSONRenderer().render(serializer.data)
        print(json_data)
        return HttpResponse(json_data,content_type='application/json')
