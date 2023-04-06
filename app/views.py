from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

# Create your views here.
def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topic.html',context=d)


def display_webpage(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='cricket')
    LOW=Webpage.objects.get(topic_name='cricket')
    LOW=Webpage.objects.all()[3:4:]
    LOW=Webpage.objects.all().order_by('name')
    LOW=Webpage.objects.all().order_by('-name')
    LOW=Webpage.objects.all().order_by(Length('name'))
    Low=Webpage.objects.all().order_by(Length('name').desc())
    LOW=Webpage.objects.all()
    d={'webpages':LOW}
    return render(request,'display_webpage.html',context=d)

def display_accessrecord(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2002-8-2')
    LOA=AccessRecord.objects.filter(date__lt='2002-8-2')
    LOA=AccessRecord.objects.filter(date__gte='2002-8-2')
    LOA=AccessRecord.objects.filter(date__lte='2002-8-2')
    d={'accessrecord':LOA}
    return render(request,'display_accessrecord.html',context=d)
