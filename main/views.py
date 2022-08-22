from email import message
from unicodedata import name
from django.shortcuts import render, redirect
from .models import chatRoom, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def lobby(request):
    title = 'Chatrooms for Private Gist'
    context = {'title':title}
    return render(request, 'lobby.html', context)

def checkRoom(request):
    room = request.POST['roomname']
    user = request.POST['chatname']

    if chatRoom.objects.filter(name=room).exists():
        return redirect('room/'+room+'/?username='+user)
    else:
        new_room = chatRoom.objects.create(name=room)
        new_room.save()
        return redirect('room/'+room+'/?username='+user)

def room(request, pk):
    title = 'Live Chat Now'
    roomname = chatRoom.objects.get(name=pk)
    username = request.GET.get('username')
    context = {'title':title, 'roomname':roomname, 'username':username}
    return render(request, 'room.html', context)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room = request.POST['room']

    new_message = Message.objects.create(message=message, user=username, room=room)
    new_message.save()

    return HttpResponse('Message sent successfully')

def getMessages(request, pk):
    room = chatRoom.objects.get(name=pk)
    messages = Message.objects.filter(room=pk)
    return JsonResponse({"messages":list(messages.values())})