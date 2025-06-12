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
from .models import room, topic,update,cash_expenditure
from .forms import RoomForm, CustomUserCreationForm
from .forms import UpdateForm, cash_expenditureForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.db.models import Sum
from .resources import updateResource
from django.core.paginator import Paginator
from django.db.models import F 
import datetime


# Create your views here.
#tips = [
    
#{'id':1,'name':'Register Here'},
#{'id':2, 'name':'Sign In Here'},
#{'id':3, 'name':'More Deatails'},


#]
def cashflow(request): 
     form = cash_expenditureForm()
     s= cash_expenditure.objects.all()
     if request.method == 'POST':
         form=cash_expenditureForm(request.POST)
         if form.is_valid():
             cash=form.save(commit=False)
             cash.save()
             return redirect('cashflow')

     context ={'form': form , 's' : s }
      
     return render(request, 'web/cash_flow.html', context)

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
    User_count= users.count()
    lists =room.objects.all()
    payment=update.objects.all()
    cash= cash_expenditure.objects.all().aggregate(total=Sum('Amount'))
    Totals = update.objects.all().aggregate(total=Sum('amount'))
    paginator = Paginator(users, 5)
    page_number = request.GET.get('page')  # Get the current page number from the URL  
    page_obj = paginator.get_page(page_number)

    
    return render(request,'web/user_list.html', {'users': users, 'page_obj' : page_obj, 'cash': cash['total'], 'lists' : lists, 'User_count': User_count, 'payment': payment, 'Totals' : Totals['total']})
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
            messages.success(request, 'success')  
            return redirect('createRoom')
     
     
    else:
           
           
             messages.error(request, 'Wrong password or username')  
            


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
    
    
  
    context ={'index': index, 'payment':payment, }
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
     
         
        
        else:
              messages.error(request, 'You have an existing profile')
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
        return redirect('createRoom')
    return render(request, 'web/delete.html', {'obj' :remove} )
def pdf(request): 
    detail=room.objects.all()
    payment=update.objects.all() 
    Totals = update.objects.all().aggregate(total=Sum('amount'))

    return render(request, 'web/pdf.html',  {'payment': payment, 'detail': detail,  'Totals' : Totals['total']})
def people(request, pk):
    detail=room.objects.get(id=pk)
    pays=update.objects.all() 
    context ={'detail':detail, 'pays': pays}
    return render(request, 'web/people.html', context)
def Panel(request):
    payment=update.objects.all() 
    detail=room.objects.all()
    context ={'detail':detail, 'payment': payment}
    return render(request, 'web/Panel.html', context)
def single(request):
    current_year = datetime.datetime.now().year
    q = request.GET.get('q') if request.GET.get('q') != None  else ''
    payment=update.objects.filter(
        Q(room__name__icontains=q) |
        Q(choice__icontains=q) |
        Q(amount__icontains=q) 
    )
    #single=update.objects.get  (id=pk)
    r_count=payment.count()
    context = {'payment': payment,'r_count':r_count }
    return render(request, 'web/import.html', context)

    

    


 
    



    






