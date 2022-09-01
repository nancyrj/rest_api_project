from django.shortcuts import render
from rest_framework.views import APIView
from .models import Students
from django.http import JsonResponse
from .serializer import Rollserializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class Student_view(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        serialiser = Rollserializer(data=request.data)
        if serialiser.is_valid(raise_exception=True):
            name=request.data.get("name")
            roll_no=request.data.get("roll_no")
            state=request.data.get("state")
            city=request.data.get("city")
            obj=Students(name=name,roll_no=roll_no,state=state,city=city)
            obj.save()
            return JsonResponse({"result_msg":"Data saved succesfully"})




class Getstudentview(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        # serialiser = Rollserializer(data=request.data)
        obj = Students.objects.all()
        print(obj)
        stud_list = []
        for i in obj:
            name=i.name
            roll_no=i.roll_no
            state=i.state
            city=i.city
            stud_list.append({"nname":name,"roll_no":roll_no,"state":state,"city":city})
        return JsonResponse({"result_msg":stud_list})
