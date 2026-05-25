from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile
from orders.models import OrderItem


def register_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(request, 'register.html')


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            return redirect('home')

    return render(request, 'login.html')


def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    # Шукаємо всі ігри з оплачених замовлень цього користувача
    purchased_items = OrderItem.objects.filter(order__user=request.user, order__is_paid=True)
    purchased_games = [item.game for item in purchased_items]

    return render(request, 'profile.html', {
        'profile': profile,
        'purchased_games': purchased_games
    })