from django import forms
from .models import *



class OrderModelForm(forms.ModelForm):
    class Meta:
        model = OrderForm
        fields = ['name', 'email', 'phone_number', 'ordercategory']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': "text",
                'placeholder': "Имя",
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': "email",
                'placeholder': "Почта",
            }),
            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': "text",
                'name': "phone",
                'placeholder': "Номер телефона",
            }),
            'ordercategory': forms.Select(attrs={
                "class": "custom-select custom-select-lg mb-3"
            })

        }