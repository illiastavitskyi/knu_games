from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from games.models import Game
from .models import Order, OrderItem
from users.models import Profile


@login_required
def add_to_cart(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    # Шукаємо неоплачене замовлення (кошик) або створюємо нове
    order, created = Order.objects.get_or_create(user=request.user, is_paid=False)

    # Додаємо гру в кошик, якщо її там ще немає
    if not OrderItem.objects.filter(order=order, game=game).exists():
        OrderItem.objects.create(order=order, game=game, price=game.price)
        order.total_price += game.price
        order.save()

    return redirect('cart')


@login_required
def view_cart(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    return render(request, 'cart.html', {'order': order})


@login_required
def checkout(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    profile, created = Profile.objects.get_or_create(user=request.user)

    if order and profile.balance >= order.total_price:
        profile.balance -= order.total_price
        profile.save()

        order.is_paid = True  # Відмічаємо кошик як оплачений
        order.save()
        return redirect('profile')

    return render(request, 'cart.html', {'order': order, 'error': 'Not enough balance'})