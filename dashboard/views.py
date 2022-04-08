from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):

    fruits = ["apple", "orange", "mango"]

    context = {
        "name": "Jhon Rhay",
        "address": "Pasay City",
        "fruits": fruits,
        "title": "Home"
    }

    return render(request, 'dashboard/home.html', context)


def about(request):

    return render(request, 'dashboard/about.html')
