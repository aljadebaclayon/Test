from django.shortcuts import render
from .models import Room

# Create your views here.

rooms = [
    {'id':1, 'name':'LEts learn python'},
    {'id':2, 'name':'Gwapo ko'},
    {'id':3, 'name':'Modejar.com'},
]


def home(request):
    rooms = Room.objects
    context = {'rooms': rooms}
    return render(request, 'MyApp/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'MyApp/room.html', context)