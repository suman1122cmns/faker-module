from pydoc_data.topics import topics
from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topics(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    return render(request,'display_topics.html',d)
def display_webpages(request):
    webpages=webpages.objects.all()
    d={'ws':webpages}
    return render(request,'display_webpages.html')   
