import keyword
import string

from django.shortcuts import render, redirect
from .models import RoomCategory, ServiceType, CaruselImage, CaruselDetail, GallaryCategory, GallaryDetail, Orders
from .serializers import ServicePriceSerializers, RoomCategorySerializers, OrdersSerialiser
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import OrderModelForm, ContactModelForm


class RoomCategoryAPIView(APIView):
    def get(self, request):
        return Response({
            'categoryroom': RoomCategorySerializers(RoomCategory.objects.all(), many=True).data
        })

    def post(self, request):
        data = OrdersSerialiser(data=request.data)
        if data.is_valid():
            return Response({
                'status': "Post qo'shildi",
                'data': data.errors
            })
        data.save()
        return Response({
            'status': 'success',
            'data': OrdersSerialiser(data.instance).data
        })


class ServicePriceAPIView(APIView):
    def get(self, request):
        return Response({
            'servicecategoryprice': ServicePriceSerializers(ServiceType.objects.all(), many=True).data
        })

    def post(self, request):
        data = OrdersSerialiser(data=request.data)
        if data.is_valid():
            return Response({
                'status': "Post qo'shildi",
                'data': data.errors
            })
        data.save()
        return Response({
            'status': 'success',
            'data': OrdersSerialiser(data.instance).data
        })




def home(request):
    caruselimg = CaruselImage.objects.filter()
    form = OrderModelForm()
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        # print("QWERTYTREAWERT------------", form)
        if form.is_valid():
            print('AAAAAAAAA------', form)
            form.save()
            return redirect('myprint:home')
        else:
            print("TTTTTTTTTTTT------------>>>>>>>", form.errors)
            form = OrderModelForm()
            print("SSSSSSSSSSSSSS------------>>>>>>>", form.errors)
    context = {
        'form': form,
        'caruselimg': caruselimg,

    }
    return render(request, 'main/index.html', context=context)


def product_detail(request, pk):
    detailCarusel = CaruselDetail.objects.filter(caruselimage_id=pk)
    context = {
        'detailCarusel': detailCarusel
    }
    return render(request, 'main/product-detail.html', context=context)

def about(request):
    return render(request, 'main/about.html')


def contact(request):
    form = ContactModelForm()
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myprint:home')
        else:
            form = ContactModelForm()
    context = {
        'form': form
    }
    return render(request, 'main/contact.html', context=context)




def gallary(request):
    gallary_page = GallaryCategory.objects.all()
    context = {
        'gallary_page': gallary_page
    }
    return render(request, 'main/gallary.html', context=context)

def gallary_details(request):
    return render(request, 'main/gallary-datails.html')


def guests(request):

    return render(request, 'main/guests.html')

# def services(request):
#     return render(request, 'main/services.html')

# def services(request):
#     cat = RoomCategory.objects.all()
#     pr = Price.objects.all()
#     if request.method == "POST":
#         check = request.POST.getlist('checks[]')
#         option = request.POST.getlist('option[]')
#         print("WWWWWWWWWWW_______>>>>>>>>>", check)
#         print("OOOOOOOOOOO_______>>>>>>>>>", option)
#         # req_obj = Orders.objects.create(nameroom=option, nameservice=check)
#         # req_obj.save()
#         return redirect('myprint:services')
#     context = {
#         'cat': cat,
#         'pr': pr
#     }
#     return render(request, 'main/services.html', context=context)


def services(request):
    cat = RoomCategory.objects.all()
    pr = ServiceType.objects.all()
    if request.method == "POST":
        services = request.POST.getlist('checks[]')
        house = request.POST.get('option[]').split("-")
        print("aaaaaaaaaaaa-------------", house)
        house_name = house[0]
        house_price = int(house[1])
        for service in services:
            service = service.split("-")
            service_name = service[0]
            service_price = service[1]
            new_order = Orders.objects.create(roomname=house_name, roomprice=house_price, servicename=service_name, serviceprice=service_price)
            new_order.save()
        return redirect('myprint:services')
    context = {
        'cat': cat,
        'pr': pr
    }
    return render(request, 'main/services.html', context=context)