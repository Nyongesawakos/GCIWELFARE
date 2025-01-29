from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from .models import user
from django.contrib.auth import authenticate, login, logout
from .models import tips
from .models import room, topic,update
from .forms import RoomForm, CustomUserCreationForm
from .forms import UpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


# Create your views here.
#tips = [
    
#{'id':1,'name':'Register Here'},
#{'id':2, 'name':'Sign In Here'},
#{'id':3, 'name':'More Deatails'},


#]
def insert(request):
    form=UpdateForm()
    if request.method == 'POST':
        form=UpdateForm(request.POST)
        if form.is_valid():
            update=form.save(commit=False)
            
            update.save()
            return redirect('user_list')
    context ={'form': form}
    return render(request, 'web/insert.html', context)
def user_list(request):
    users = User.objects.all()
    lists =room.objects.all()
    payment=update.objects.all()
    return render(request,'web/user_list.html', {'users': users, 'lists' : lists, 'payment': payment})
def loginPage(request):
    page= 'login'
    if request.user.is_authenticated: 
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User= user.objects.get(username=username)
        except:
            messages.error(request, '')
            User = authenticate(request, username=username, password=password)
            if User is not None:
                login(request, User)
                return redirect('home')
            else:
              messages.error(request, 'Wrong password or username')  
    context = {'page' : page}
    return render(request,'web/registration_login.html',context)
def logoutUser(request):
    logout(request)
    return redirect('login')
def registerPage(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
     form = CustomUserCreationForm(request.POST)
     if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
     
     
    else:
           
            messages.error(request, 'Register with Correct details')
            


    return render(request,'web/registration_login.html', { 'form' : form})

def home(request): 
    q = request.GET.get('q') if request.GET.get('q') != None  else ''
    tips = room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)|
        Q(lastName__icontains=q) 
        
        
                                     
                                )
    
    topics=topic.objects.all()
    users = User.objects.all()
    room_count= tips.count()
    context ={'tips': tips, 'topics': topics, 'room_count' : room_count, 'users' : users}
    return render(request, 'web/home.html', context)

def index(request, pk):
    index= room.objects.get(id=pk)
    payment= update.objects.all()
  
    context ={'index': index, 'payment':payment}
    return render(request, 'web/index.html', context)
@login_required(login_url='/login')
def createRoom(request):
    form= RoomForm()
    if request.method == 'POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            room=form.save(commit=False)
            room.host=request.user
            room.save()
            return redirect('home')
    context = {'form' : form}
    return render(request, 'web/room_form.html', context)
@login_required(login_url='/login')
def updateRoom(request, pk):
    update = room.objects.get(id=pk)
    form=RoomForm(instance=update)
    if request.user != update.host:
        return HttpResponse('You are not allowed here')
    if request.method == 'POST':
        form=RoomForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('home')
    context= {'update' : update, 'form' : form}
    return render(request, 'web/room_form.html', context)
@login_required(login_url='/login')
def deleteRoom(request, pk):
    remove=room.objects.get(id=pk)
    if request.method == 'POST':
        remove.delete()
        return redirect('home')
    return render(request, 'web/delete.html', {'obj' :remove} )

    



    






