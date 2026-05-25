from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from orders.models import OrderItem

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    purchased_items = OrderItem.objects.filter(order__user=request.user, order__is_paid=True)
    purchased_games = [item.game for item in purchased_items]

    return render(request, 'profile.html', {
        'profile': profile,
        'purchased_games': purchased_games
    })

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def deposit_funds(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        if amount:
            try:
                deposit_amount = Decimal(amount)
                if deposit_amount > 0:
                    # Використовуємо get_or_create для уникнення помилки DoesNotExist
                    profile, created = Profile.objects.get_or_create(user=request.user)
                    profile.balance += deposit_amount
                    profile.save()
            except ValueError:
                pass

    return redirect('profile')