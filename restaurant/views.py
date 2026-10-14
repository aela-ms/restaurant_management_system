from django.shortcuts import render


def home(request):
    return render(request, 'restaurant/home.html')


def menu(request):
    return render(request, 'restaurant/menu.html')


def about(request):
    return render(request, 'restaurant/about-us.html')


def reservation(request):
    return render(request, 'restaurant/reservation.html')


def contact(request):
    return render(request, 'restaurant/contact.html')

def gallery(request):
    return render(request, 'restaurant/gallery.html')
