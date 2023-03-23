from rest_framework import serializers
from .models import Complaints
from state_city.models import States,Cities
from users.models import Users

class ComplaintSerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField('get_state')

    def get_state(self,obj):
        try:
           state=States.objects.get(state_id = obj.state_id.state_id)
           print(state)
           return state.state_name
        except Exception as e:
           print(e)
           return ""


    class Meta:
        model= Complaints
        fields = '__all__'

# class AdminHomeSerializer(serializers.Serializer):
#     total_issues = serializers.SerializerMethodField('get_total_issues')
#     # total_issues_resolved = serializers.SerializerMethodField('get_total_issues_resolved')
#     # total_issues_pending = serializers.SerializerMethodField('get_total_issues_pending')
#     total_cities_connected = serializers.SerializerMethodField(method_name='get_total_cities_connected')
#     total_officers = serializers.SerializerMethodField(method_name='get_total_officers')
#     total_users = serializers.SerializerMethodField(method_name='get_total_users') 

#     def get_total_cities_connected():
#         try:
#            total_cities = Cities.objects.all().count()
#            return total_cities
#         except:
#            total_cities=0 
#            return total_cities

#     def get_total_officers():
#         try:
#            total_officers = Users.objects.filter(role='officer').count()
#            return total_officers
#         except:
#            total_officers=0 
#            return total_officers 

#     def get_total_users():
#         try:
#            total_users = Users.objects.all().count()
#            return total_users
#         except:
#            total_users=0 
#            return total_users

#     def get_total_issues():
#         try:
#            total_issues = Complaints.objects.all().count()
#            return total_issues
#         except:
#            total_issues=0 
#            return total_issues  
                    

    # def get_total_users():
    #     try:
    #        total_users = Users.objects.all().count()
    #        return total_users
    #     except:
    #        total_users=0 
    #        return total_users


    # def get_total_users():
    #     try:
    #        total_users = Users.objects.all().count()
    #        return total_users
    #     except:
    #        total_users=0 
    #        return total_users