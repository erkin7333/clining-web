from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def gallary_details(request):
    return render(request, 'main/gallary-details.html')

def gallary(request):
    return render(request, 'main/gallary.html')


def guests(request):
    return render(request, 'main/guests.html')







def services(request):
    room = RoomCategory.objects.all()
    service = ServiceType.objects.all()
    form = OrderForm()

    if request.method=="POST":
        form = OrderForm()
        name=request.POST.get("name")
        price=request.POST.get("price")
        # print("->>>>>>>>>>>>>>>>>>", name, price)
        obj = Double.objects.create(name=name, price=price)
        obj.save()
        return redirect('myprint:home')
    else:
        pass
    context = {'room': room,
               'service': service,
               'form': form}
    return render(request, 'main/services.html', context=context)









def service_count(request):
    form = OrderForm()
    if request.method=="POST":
        form = OrderForm()
        form = Double.objects.create(name=request.POST.get("rooms"), price=request.POST.get("price"))
        form.save()
        return redirect('myprint:home')

    context = {'form': form}
    return render(request, 'main/service_count.html', context=context)