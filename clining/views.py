from django.shortcuts import render

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
    return render(request, 'main/services.html')