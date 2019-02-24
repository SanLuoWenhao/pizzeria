from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.http import HttpResponse

from pizzeriaApp.models import Pizza, Topping


def index(request):
    return render(request, 'pizzeriaApp/index.html')


def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzeriaApp/pizzas.html', context)


def toppings(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = Topping.objects.get(id=pizza_id)
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzeriaApp/toppings.html', context)