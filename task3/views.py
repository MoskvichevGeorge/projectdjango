from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'third_task/home.html')

def shop(request):
    items = {
        'item1': 'Atomic Heart',
        'item2': 'Grand Theft Auto V',
        'item3': 'Rust',
    }
    return render(request, 'third_task/shop.html', {'items': items})

def basket(request):
    return render(request, 'third_task/basket.html')
