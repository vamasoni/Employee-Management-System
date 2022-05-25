from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Member
from django.contrib.auth import get_user_model

#from django.contrib import messages

# Create your views here.

def register(request):

    if request.method =='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        emailid=request.POST['emailid']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                context = {'msg': 'Username Taken'}
                #messages.info(request, 'Username taken')
                return render(request, 'register.html', context)
                #return redirect('register')

            elif User.objects.filter(email=emailid).exists():
                context = {'msg': 'Email-ID Taken'}
                return render(request, 'register.html', context)
                # messages.info(request, 'Email-ID Taken')
                # return redirect('register')

            else:
                user=User.objects.create_user(username=username, password=password1, email=emailid, first_name=firstname, last_name=lastname)
                user.save()
                member = Member(username=username, password=password1, emailid=emailid, firstname=firstname, lastname=lastname)
                member.save()
                context = {'msg': 'User Created'}
                return render(request, 'register.html', context)
                # messages.success(request, 'User Created!')
        else:
            context = {'msg': 'Password not matching'}
            return render(request, 'register.html', context)
    else:
        return render(request, 'register.html') 
"""
def home(request):
    if request.method == 'POST':

        if Member.objects.filter(username=request.POST['username'], password=request.POST['password1']).exists():
            member = Member.objects.get(username=request.POST['usename'], password=request.POST['password1'])
            return render(request, 'home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)
 """
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user = auth.authenticate(username=username, password = password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'login.html', context)
            
    else:
        return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def details(request):
    id=request.POST['id']
    # context ={}
    # context["data"]=Member.objects.get(id = id)
    # return render(request, 'details.html', context)
    member = Member.objects.get(id=id)
    context = {'member': member}
    return render(request, 'details.html', context)

def change_password(request):
        return render(request, 'change_password.html')

def change_pwd(request):
        # oldpass=request.POST['oldpass']
        # current=request.POST['password']
        newpass1=request.POST['newpass1']
        newpass2=request.POST['newpass2']

        if newpass1 != newpass2:
            context = {'msg': 'Password not matching'}
            return render(request, 'change_password.html', context)
        
        else:
            id=request.POST['id']            
            # print(id)
            user=User.objects.get(id=id)
            user.set_password(newpass1)
            user.save()
            # member=Member.objects.get(id=id)
            # member.set_password(newpass1)
            # member= Member(password=newpass1)
            # member.save()
            context = {'msg': 'Password Changed!'}
            return render(request, 'change_password.html', context)

def update(request):
    newfirstname=request.POST['newfirstname']
    newlastname=request.POST['newlastname']
    newemail=request.POST['newemail']
    newusername=request.POST['newusername']
    id=request.POST['id']
    user=User.objects.get(id=id)
    user.first_name=newfirstname
    user.last_name=newlastname
    user.username=newusername
    user.email=newemail
    user.save()
    context = {'msg': 'Your account has been updated successfully'}
    return render(request, 'details.html', context)

def user_details(request):
    # user=User.objects.get()
    # context = {'user': user}
    all_user = User.objects.all().order_by('id')
    for data in all_user:
        print(data.id)
    return render(request, 'user_details.html', {'userr': all_user})  
    



