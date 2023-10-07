from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .models import FormSubmission



# Create your views here.
def login_page(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username ,password=password )

        if user is not None:
           login(request,user)
           return redirect('/')
    
        else :
            message = "something wrong with your account"

            return render(request,'login.html' ,{ 'message' : message ,})


    return render(request,"login.html")



def register(request):
    if request.method=="POST":
     
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']

      if User.objects.filter(username=username).exists():
        
        return render( request,'login.html')
      else:
        User_object = User.objects.create(
           username = username ,
           email = email )
        User_object.set_password(password)
        User_object.save()

        return render(request,"login.html")
      
    
    
    return render(request,"register.html")


    
        

    
    


@login_required()
def home(request):
    return render(request,"home.html")

def updateTask(request):
    return render(request,"update.html")

def history(request):
    return render(request,"history.html")

def logout_page(request):
    logout(request)
    return redirect('/login/')

@login_required()
def adddata(request):
    if request.method == 'POST':
        # Create a new FormSubmission instance and associate it with the logged-in user
        create_capm = FormSubmission.objects.create(
            user  =request.user,
            campname = request.POST['campname'],
            idname = request.POST['idname'],
            amount = request.POST['amount'],
        )
        create_capm.save()
        # Add code to handle and save other form data to the FormSubmission model
        # form_submission.field_name = request.POST['field_name']
        

        return render(request,"add.html")
    
    return render(request,"add.html")


    