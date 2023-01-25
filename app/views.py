from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topics(request):
    a=Topic.objects.all()
    d={'topics':a}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    b=Webpage.objects.all()
    d={'webpages':b}
    return render(request,'display_webpages.html',d)

def display_Access_Records(request):
    c=Access_Records.objects.all()
    d={'records':c}
    return render(request,'access_record.html',d)