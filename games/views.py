from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import GameForm

def landing(request):
    return render(request, 'landing.html')


def home(request):
    return render(request, 'home.html')



def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def add_game(request):
    if request.method == 'POST':
        # request.FILES обов'язковий для збереження фотографій!
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = GameForm()
    return render(request, 'add_game.html', {'form': form})


from .models import Game


def catalog(request):
    games = Game.objects.all()

    # Отримуємо параметри фільтрації з URL
    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    release_date = request.GET.get('release_date')

    # Застосовуємо фільтри, якщо користувач їх ввів
    if category:
        games = games.filter(category__icontains=category)
    if min_price:
        games = games.filter(price__gte=min_price)
    if max_price:
        games = games.filter(price__lte=max_price)
    if release_date:
        games = games.filter(release_date__gte=release_date)

    return render(request, 'catalog.html', {'games': games})