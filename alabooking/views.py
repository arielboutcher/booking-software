from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import CreateUserForm, BookingForm

def home(request):
    return render(request, 'booking.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    return render(request, 'booking.html')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user )
            return redirect('login')


    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password = password)
        if user is not None:

            login(request, user)
            user_id = user.id
            messages.success(request, 'User has been logged in.')
            return redirect('profile', pk= user_id)
        else:
            messages.error(request, 'Username or password is incorrect')


    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request, pk):
    user  = User.objects.get(id=pk)
    name = user.username

    ############modal booking form
    booking_form = BookingForm()
    rooms = Room.objects.all()

    if request.method == "POST":
        booking_form = BookingForm(request.POST)
        dateToBeUsed = request.POST.get('date')
        timeToBeUsedFrom = request.POST.get('timefrom')
        timeToBeUsedTo = request.POST.get('timeto')
        if booking_form.is_valid:
            #dateToBeUsed = request.POST.get('date')
            #timeToBeUsedFrom = request.POST.get('timefrom')
            #timeToBeUsedTo = request.POST.get('timeto')
            booking_form.save()
            booking_id = booking_form.cleaned_data.get('id')
            message = messages.success(request, 'Booking was made with Booking ID '+booking_id )
            return redirect('profile')
        else:
            message=messages.error(request, 'Booking has failed!')
            ##end of booking modal form

    context = {
    'name':name,
    'form':booking_form,
    'rooms':rooms,
    }
    return render(request, 'profile.html', context)

#################################################################3

"""
@login_required
def createBooking(request):
    booking_form = BookingForm()
    rooms = Room.objects.all()

    if request.method == "POST":
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid:
            booking_form.save()
            booking_id = booking_form.cleaned_data.get('id')
            messages.success(request, 'Booking was made with Booking ID '+booking_id )
            return redirect('profile')
        else:
            messages,error(request, 'Booking has failed!')

    context = {'form':booking_form, 'rooms':rooms}

    render(request, 'booking.html', context)
"""
