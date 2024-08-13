from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')
def loginpage(request):
    return render(request,'login.html')

def about(request):
    # if request.user.is_authenticated:
    #     return render(request,'about.html') using Is_authenticated
    # else:
        return render(request,'about.html')
    # if 'uid' in request.session:
    #     return render(request,'about.html')
    # else:
    #     return render(request,'login.html')    about page using session
    

def usercreate(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
        else:
            messages.info(request, 'Password not matching')
            print("Password not matching")
            return redirect('signup')
        return redirect('loginpage')
    return render(request, 'signup.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_staff:
                 login(request,user)
                 return redirect('adm')
            else:
                 auth.login(request, user)
                 messages.info(request, f'welcome {username}')
                 return redirect('about')
                 
            # request.session["uid"]=user.id using session
            
        else:
            messages.info(request, 'invalid username or password')
            return redirect('loginpage')

    return render(request, 'login.html')


def logout(request):
    # if request.user.is_authenticated:   using Is_authenticated 
    # request.session["uid"] = "" using session
        auth.logout(request)
        return redirect('home')

def adm(request):
    return render(request,'admin.html')


