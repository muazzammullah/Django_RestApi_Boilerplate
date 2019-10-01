from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import json
#########################
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework import serializers
########################
from .models import Employee

def index_api_response(request):
	responseData = {
    	'Error':'Endpoint not found:Append Endpoint' ,
	}
	return HttpResponse(json.dumps(responseData), content_type="application/json")


class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Employee
		fields='__all__'

class EmployeeListView(APIView):
	def get(self,request):
		employees=Employee.objects.all()
		serializer=EmployeeSerializer(employees,many=True)
		return Response(serializer.data)
	def post(self,request):
		pass
