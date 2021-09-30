from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from .models import employee

# Create your views here.

def register(request):
    #  new employee adding function
    if request.method == 'POST':
        # here getting from html 
        emp =employee()
        emp.s_id = request.POST['SINO']
        emp.name = request.POST['name']
        # emp.image = request.POST.get['image']
        emp.email = request.POST['email']
        emp.password = request.POST['password']
        emp.phone = request.POST['phone']
        emp.address = request.POST['address']

        #  here checking image selected or not
        if len(request.FILES['image']) != 0:
            emp.image = request.FILES['image']

        # checking email is already exists or not.if exist then redirect to register page
        if (User.objects.filter(email = emp.email).exists()):
            messages.Warning(request,'This Email already exists')
            return redirect('register.html')

        # otherwise save the data to database and also redirect to register page
        else:
            # user = User.objects.create_user( id =emp.s_id,username = emp.name,image = emp.image,email = emp.email,password = emp.password,phone = emp.phone,address = emp.address)
            # user.save();
            emp.save()
            messages.Info(request,'employee added successfully')
            # message passing to user
            meg='employee added successfully'
            return redirect('register.html',{'message':meg})
    else:
        # if error occur then message passing user and redirect to register page
        message = 'error....employee not added'
        return render(request,'register.html',{'message' : message})
