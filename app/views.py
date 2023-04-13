from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q


# Create your views here.
def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topic.html',context=d)


def display_webpage(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='cricket')
    LOW=Webpage.objects.all()[3:4:]
    LOW=Webpage.objects.all().order_by('name')
    LOW=Webpage.objects.all().order_by('-name')
    LOW=Webpage.objects.all().order_by(Length('name'))
    Low=Webpage.objects.all().order_by(Length('name').desc())
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__startswith='d')
    LOW=Webpage.objects.filter(name__endswith='i')
    LOW=Webpage.objects.filter(name__contains='S')
    LOW=Webpage.objects.filter(url__contains='.in')
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{7}')
    LOW=Webpage.objects.filter(name__in=('dhoni','kohli'))
    #LOW=Webpage.objects.filter(Q(topic_name='cricket') & Q(name='dhoni'))
    LOW=Webpage.objects.all()
    d={'webpages':LOW}
    return render(request,'display_webpage.html',context=d)

def display_accessrecord(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2002-8-2')
    LOA=AccessRecord.objects.filter(date__lt='2002-8-2')
    LOA=AccessRecord.objects.filter(date__gte='2002-8-2')
    LOA=AccessRecord.objects.filter(date__lte='2002-8-2')
    LOA=AccessRecord.objects.all()
    LoA=AccessRecord.objects.filter(date__year='2022')
    LOA=AccessRecord.objects.filter(date__month__gt='8')
    LOA=AccessRecord.objects.filter(date__day__lt='2')
    LOA=AccessRecord.objects.all()
    d={'accessrecord':LOA}
    return render(request,'display_accessrecord.html',context=d)


def update_webpage(request):
    #Webpage.objects.filter(name='dhoni').update(email='dhoni@gmail.in')

    #Webpage.objects.filter(topic_name='cricket').update(email='MSD@gmail.com')
    #Webpage.objects.filter(name='Zehra').update(topic_name='chess')
    #Webpage.objects.update_or_create(email='MSD@gmail.com',defaults={'name':'MSD'})
    TO=Topic.objects.get_or_create(topic_name='cricket')[0]
    TO.save()
    Webpage.objects.update_or_create(name='pandya',defaults={'topic_name':TO,'url':'https://hardik.com','email':'hardik@gmail.com'})
    d={'webpage':Webpage.objects.all()}
    return render(request,'dispaly_webpage.html',d)



def delete_webpage(request):
    #Webpage.objects.filter(name='kohli').delete()
    #Webpage.objects.filter(name='hardik').delete()
    #Webpage.objects.filter(email='MSD@gmail.com').delete()
    Webpage.objects.all().delete()
    d={'webpage':Webpage.objects.all()}

    return render(request,'display_webpage.html',d)
