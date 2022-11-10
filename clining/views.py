import string

from django.shortcuts import render, redirect
from .models import RoomCategory, Price, ServiceType, Orders


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
    cat = RoomCategory.objects.all()
    pr = Price.objects.all()
    if request.method == "POST":
        check = request.POST.getlist('checks[]')
        option = request.POST.getlist('option[]')
        print("WWWWWWWWWWW_______>>>>>>>>>", check)
        print("OOOOOOOOOOO_______>>>>>>>>>", option)
        req_obj = Orders.objects.create(nameroom=option, nameservice=check)
        req_obj.save()
        return redirect('myprint:services')
    context = {
        'cat': cat,
        'pr': pr
    }
    return render(request, 'main/services.html', context=context)