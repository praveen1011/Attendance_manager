from django.http import HttpResponseRedirect,request,HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django import forms
from .models import logins
import json

def home(request):
    return render(request,'AIT2020/Home.html')
def check(request):
    login = logins.objects.get(faculty_id=request.GET["userid"])
    if (login.password == request.GET["password"]):
        r = {"result" : "success"}
        return HttpResponse(json.dumps(r),content_type="application/json")
    else:
        r = {"result": "failed"}
        return HttpResponse(json.dumps(r),content_type="application/json")