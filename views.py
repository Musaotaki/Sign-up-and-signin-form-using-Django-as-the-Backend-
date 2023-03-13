from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User

# Create your views here.

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'EMAIL ALREADY EXIST')
                return redirect('/')
                
            else: 
                user = User.objects.create_user(username=name, email=email, password=password)
                user.email = email
                user.username = name 
                user.save()
                return redirect('signin')
        else:
            messages.info(request, 'PASSWORD DOES NOT MATCH')
            return redirect('/')
  
                       
    else:
        return render(request, 'signup.html')
    
    
def signin(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password = password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('welcome')
        else:        
            messages.info(request, 'INVALID CREDENTIALS')
            return redirect('signin') 
           
    else:   
        return render(request, 'signin.html')
        
def welcome(request):
   
    return render(request, 'welcome.html')
    
def logout(request):
    auth.logout(request)
    return redirect('signin')
    
