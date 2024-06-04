from django.shortcuts import render, redirect

from api.models import Circuit


# Create your views here.
def index(request):
    return render(request, 'index2.html', context={})


def circuits(request):
    return render(request, 'index2.html', {'circuits': Circuit.objects.all()})
