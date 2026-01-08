from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from website.models import Contact
from website.forms import NameForm , ContactForm, NewsleterForm
from django.contrib import messages

def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.success, 'your ticket submited successfully')
        else:
            messages.add_message(request,messages.ERROR, 'your ticket didnt submited')

            return redirect('website:contact')  # خیلی مهم
    else:
        form = ContactForm()
    
    return render(request,'website/contact.html', {'form':form})

def newsleter_view(request):
    if request.method == 'POST':
        form = NewsleterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


# Create your views here.
