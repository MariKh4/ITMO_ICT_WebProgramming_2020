from django.shortcuts import render
from django.http import Http404
import datetime
from .models import *
from django.views.generic.list import ListView
from .forms import *
from django.views.generic.edit import CreateView


class GeeksList(ListView):
    model = GeeksModel

def list_view(request):
    context ={}
    context["dataset"] = GeeksModel.objects.all()    
    return render(request, "list_view.html", context)

def detail(request, poll_id):
    try:
        p = User.objects.get(pk=poll_id)
    except User.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'owner.html', {'owner': p})


def geeks_view(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)
    return HttpResponse(html)

def CarOwnerList(request):
    context ={}
    context["dataset"] = User.objects.all()    
    return render(request, "CarOwnerList.html", context)

class CarList(ListView):
    model = Car

def create_view(request):
    context ={}
    form = GeeksForm(request.POST or None) 
    if form.is_valid(): 
        form.save()
    context['form']= form
    return render(request, "create_view.html", context)

  
class GeeksCreate(CreateView):
    model = GeeksModel
    fields = ['title', 'description']


def carowner_create_view(request):
    context ={}
    form = CarsOwnerForm(request.POST or None) 
    if form.is_valid(): 
        form.save()
    context['form']= form
    return render(request, "create_view.html", context)

  
class CarCreate(CreateView):
    model = Car
    fields = ['mark', 'model', 'color', 'state_number']


