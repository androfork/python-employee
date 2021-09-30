from django.core.checks import messages
from django.shortcuts import redirect, render
from details.models import employee
from django.contrib.auth.models import User,auth
from details.models import employee

def index(request):
    em = employee.objects.all()
    # get all data from database
    return render(request,'index.html',{'em':em})
    #  passing data to home page 

def reg(request):
    #  view function for register
    return render(request,'register.html')

def home(request):
    #  view function for home page
    return render(request,'home.html')

def login(request):
    # login function 
    # getting username / email or password from login.html page
    if request.method == 'POST' :
        username = request.POST['username']     
        password = request.POST['password']  

        user = auth.authenticate(username = username , password = password)
        # checking user is valid or not OR user authentication of admin
        #  here take the user name and password

        try:
            Userdetail = employee.objects.get(email=request.POST['username'],password = request.POST['password'])
            # here checking email and password of abc company
            request.session['email'] = Userdetail.email
            return render(request,'home.html')
            #  if user valid go to home page

        except employee.DoesNotExist as e:
            messages.Info(request,'invalid username and password') 
            #  if user is not valid then passing message to to user

        if user is not None:
            auth.login(request,user)
            return redirect('home.html')
            # if admin is valid then redirect home page

        else:
            messages.Info(request,'invalid username or password')
            message='invalid username or password'
            return redirect('login.html',{'message' :message})
            # if the admin is invalid than pass message and also rediect to home page 
    else:
        auth.logout(request)
        return render(request,'login.html')
        #  otherwise logout and  redirect to home page