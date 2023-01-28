
from django.http import HttpResponse
from django.shortcuts import render


def HomePage(request):
    return render (request,"index.html",data)

def course(request):
    return HttpResponse('welcome')
 
def courseDetails(request,courseid):
    return HttpResponse(courseid)

