from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Signupform,loginform,inpform,editform
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as django_login
from todoapp.models import todo

# Create your views here.
def home(request):
    form = inpform()
    alldata = todo.objects.all()[:4]
    
    if request.method == 'POST':
        form = inpform(request.POST)
        tit = request.POST.get('Title')
        dat = request.POST.get('Date')
        stat = request.POST.get('status')
        print(stat)
        #print(f'Title = {tit} , date = {dat}')
        todo.objects.create(Title=tit, date=dat, status=stat)
        alldata = todo.objects.all()
        print(alldata)
        return redirect('home')
    return render(request,'todoapp/index.html',{'form':form,'data':alldata})
def todolist(request):
    alldata = todo.objects.all()
    print(alldata)
    return render(request,'todoapp/show.html',{'data':alldata})
def signup(request):
    form = Signupform()
    if request.method == 'POST':
        form = Signupform(request.POST)
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        print(pass1,pass2)
        if pass1 != pass2:
            return HttpResponse('password not matched') 
        elif form.is_valid():
            userr = User.objects.create_user(username=uname, email=email, password=pass1)
            return redirect('login')
    return render(request,'todoapp/signup.html',{"form":form})
def login(request):
    form = loginform()
    if request.method == 'POST':
        form = loginform(request.POST)
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(request,username=uname,password=passw)
        print(uname,passw)
        if user is not None:
            django_login(request,user)
            return redirect(home)
    return render(request,'todoapp/login.html',{'form':form})
def selectedit(request):
    alldata = todo.objects.all()
    return render(request,'todoapp/selectedit.html',{'data':alldata})
def selectdelete(request):
    alldata = todo.objects.all()
    return render(request,'todoapp/selectdelete.html',{'data':alldata})
def edit(request,pk):
    form = editform()
    alldata = todo.objects.all()  # Fetch all objects
    prikey = todo.objects.get(id=pk)
    if request.method == 'POST':
        form = editform()
    return render(request,'todoapp/edit.html',{'form':form,'data':alldata,'key':prikey})
def updatedata(request,pk):
    data = todo.objects.get(id=pk)
    data.Title = request.POST.get("Title")
    data.date = request.POST.get("date")
    data.status = request.POST.get("status")
    data.save()
    return redirect('home')
def delete(request,pk):
    ddata = todo.objects.get(id=pk)
    ddata.delete()
    return redirect('todolist')
def status(request):
    alldata = todo.objects.all()
    return render(request,'todoapp/status.html',{'data':alldata})

