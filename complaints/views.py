from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ComplaintSerializer
from .models import Complaints
from rest_framework.response import Response
from users.models import Users
from state_city.models import Cities
from django.http import HttpResponseBadRequest

# Create your views here.


@api_view(['GET'])
def AllComplaints(request):
    if request.method == 'GET':
        complaints = Complaints.objects.all()
        serializer = ComplaintSerializer(complaints,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def AllOfficerComplaints(request, id):
    if request.method == 'GET':
        officer = Users.objects.get(id=id)
        total_complaints = Complaints.objects.filter(city_id=officer.city_id)
        serializer = ComplaintSerializer(total_complaints, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def AdminHome(request):
    if request.method == 'GET':
      try:
        total_users = Users.objects.count()
        total_officers = Users.objects.filter(role='officer').count()
        total_issues = Complaints.objects.all().count()
        total_issues_pending = Complaints.objects.filter(progress__lt = 100).count()
        total_issues_resolved = Complaints.objects.filter(progress=100).count()
        total_cities = Cities.objects.all().count()
        jsonResponse = {
         "total_users":total_users,
         "total_officers":total_officers,
         "total_complaints":total_issues,
         "total_complaints_pending":total_issues_pending,
         "total_complaints_resolved":total_issues_resolved,
         "total_cities":total_cities 
        }
        return Response(jsonResponse)
      
      except Exception as e:
        jsonResponse = {
         "total_users":"",
         "total_officers":"",
         "total_complaints":"",
         "total_complaints_pending":"",
         "total_complaints_resolved":"",
         "total_cities":"" 
        }
        print(e)
        return Response()    
    
    return HttpResponseBadRequest    


@api_view(['GET'])
def OfficerHome(request, id):
    if request.method == 'GET':
        officer = Users.objects.get(id=id)
        print(officer.city_id)
        try:
            officer_total = Complaints.objects.filter(city_id=officer.city_id).count()
            officer_total_pending_issues = Complaints.objects.filter(city_id=officer.city_id,
                                                                     progress__lt="100").count()
            officer_total_resolved_issues = Complaints.objects.filter(city_id=officer.city_id,
                                                                      status="completed").count()
            users_under_officer = Users.objects.filter(city_id=officer.city_id).distinct().count()
            users_under_officer -= 1
            jsonResponse = {
                "user_under_officers": users_under_officer,
                "total_complaints": officer_total,
                "total_complaints_pending": officer_total_pending_issues,
                "total_complaints_resolved": officer_total_resolved_issues
            }
            return Response(jsonResponse)

        except Exception as e:
            jsonResponse = {
                "user_under_officers": "",
                "total_complaints": "",
                "total_complaints_pending": "",
                "total_complaints_resolved": ""
            }
            print(e)
            return Response(jsonResponse)
    return HttpResponseBadRequest


@api_view(['POST'])
def AddComplaint(request):
    if request.method == 'POST':
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response({"Message":"Your Complaint is registered successfully"})
        else:
          return Response(serializer.errors)  

    return HttpResponseBadRequest()


@api_view(['GET'])
def LatestComplaints(request):
    if request.method == 'GET':
        complaints = Complaints.objects.order_by('-comp_id')[:2]
        serializer = ComplaintSerializer(complaints, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def PendingComplaints(request):
    if request.method == 'GET':
        pending_complaints = Complaints.objects.filter(progress__lt = 100)
        serializer = ComplaintSerializer(pending_complaints, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def ResolvedComplaints(request):
    if request.method == 'GET':
        pending_complaints = Complaints.objects.filter(status="completed")
        serializer = ComplaintSerializer(pending_complaints, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def DeleteComplaints(request, comp_id):
    if request.method == 'POST':
        try:
            complaint = Complaints.objects.get(comp_id=comp_id)
            complaint.delete()
            return Response({"message": "complaint deleted succesfully"})
        except:
            return Response({"message": "comlpaint not found"})
    return HttpResponseBadRequest()

@api_view(['GET'])
def ResolvedComplaintsOfficer(request,pk):
    if request.method == 'GET':
        pending_complaints = Complaints.objects.filter(progress=100,comp_by=pk)
        serializer = ComplaintSerializer(pending_complaints, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def UpdateComplaints(request):
    if request.method == 'POST':
        status = request.data['status']
        progress = request.data['progress']
        action_taken = request.data['action_taken']
        complaint_id = request.data['complaint_id']
        try:
            Complaints.objects.filter(comp_id=complaint_id).update(status=status, progress=progress, action_taken=action_taken)
            return Response({"message": "complaint updated succesfully","status":1})
        except Exception as e:
            print(e)
            return Response({"message": "comlpaint not found","status":0})
    return HttpResponseBadRequest()

