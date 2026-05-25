from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import GameForm
from .models import Game
from django.shortcuts import render, redirect, get_object_or_404

# Перевірка на адміна
def is_admin(user):
    return user.is_superuser

# Додавання гри адміном
@user_passes_test(is_admin)
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = GameForm()
    return render(request, 'add_game.html', {'form': form})

# Головна сторінка (розподіляє гостей та авторизованих користувачів)
def home_view(request):
    if not request.user.is_authenticated:
        return render(request, 'landing.html')
    return render(request, 'home.html')

# Каталог з фільтрами
def catalog(request):
    games = Game.objects.all()

    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    release_date = request.GET.get('release_date')

    if category:
        games = games.filter(category__icontains=category)
    if min_price:
        games = games.filter(price__gte=min_price)
    if max_price:
        games = games.filter(price__lte=max_price)
    if release_date:
        games = games.filter(release_date__gte=release_date)

    return render(request, 'catalog.html', {'games': games})

def game_detail(request, game_id):
    # Шукаємо гру за її id. Якщо такої немає - покажемо сторінку 404
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'game_detail.html', {'game': game})