from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponseBadRequest, JsonResponse
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Users


# Create your views here.

@api_view(['POST'])
def AddUser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "User Registered Successfully",'status':1})
        else:
            return Response(serializer.errors)

    return HttpResponseBadRequest


@api_view(['GET'])
def DeleteUser(request,pk):
        try:
            user = Users.objects.get(id=pk)
            user.delete()
            return JsonResponse({"Message": "user " + str(pk) + " is successfully deleted"})
        except:
            return JsonResponse({"Message": "user" + str(pk) + " not found"})

@api_view(['GET'])
def AllUsers(request):
        try:
            users = Users.objects.all()
            serializer=UserSerializer(users,many=True)
            return Response(serializer.data)
        except:
            return Response({"message":"failed"})



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
