from rest_framework import serializers
from .models import Users
from state_city.models import States,Cities
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from state_city.models  import States,Cities 

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
            print('create been called')
            password = validated_data.pop('password')
            user = super().create(validated_data)
            user.set_password(password)
            user.save()
            return user

    class Meta:
        model = Users
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):


    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['user_id'] = self.user.id
        data['name'] = self.user.name
        data['email'] = self.user.email
        data['phone'] = self.user.phone
        data['country'] = self.user.country
        data['role'] = self.user.role
        data['user_id'] = self.user.id
        data['state_id'] = self.user.state_id.state_id
        data['city_id'] = self.user.city_id.city_id
        try:
            state = States.objects.get(state_id = self.user.state_id.state_id)
            city = Cities.objects.get(city_id=self.user.city_id.city_id)
            data['state'] = state.state_name
            data['city'] = city.city_name
        except Exception as e:
            print(e)
            data['state'] = ""
            data['city'] = ""   

        return data        


             




