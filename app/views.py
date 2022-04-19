from pydoc_data.topics import topics
from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topics(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    return render(request,'display_topics.html',d)
def display_webpages(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(topic_name='Foot Ball')
    #webpages=Webpage.objects.exclude(topic_name='Foot Ball')
    #webpages=Webpage.objects.all()[0:2:]
    #webpages=Webpage.objects.all()[-3]
    #webpages=Webpage.objects.all().order_by('name')
   # webpages=Webpage.objects.all().order_by('-name')
   # webpages=Webpage.objects.all().order_by(Length('name'))
    #webpages=Webpage.objects.all().order_by(Length('name').desc())
    #webpages=Webpage.objects.filter(name='virat')
    #webpages=Webpage.objects.filter(topic_name='kabaddi')
    #webpages=Webpage.objects.filter(name__startswith='s')
    #webpages=Webpage.objects.filter(name__endswith='s')
    #webpages=Webpage.objects.filter(url__startswith='https')
    d={'ws':webpages}
    return render(request,'display_webpages.html',d)

def display_access(request):
    access=AccessRecords.objects.all()
    access=AccessRecords.objects.all()
    access=AccessRecords.objects.filter(date='2020-06-26')
    access=AccessRecords.objects.filter(date__month='03')
    access=AccessRecords.objects.filter(date__month='09')
    access=AccessRecords.objects.filter(date__year='2000')
    access=AccessRecords.objects.filter(date__month__gt='03')
    access=AccessRecords.objects.filter(date__day__gte='03')
    d={'ac':access}
    return render(request,'display_access.html',d)