from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'second_task/function_view.html')


def get(request):
    return render(request, 'class_view.html')
