from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'fourth_task/home.html', {'pagename': 'Главная страница'})

def shop(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    return render(request, 'fourth_task/shop.html', {'pagename': 'Игры', 'games': games })

def basket(request):
    return render(request, 'fourth_task/basket.html', {'pagename': 'Корзина'})
