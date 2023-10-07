from django.shortcuts import redirect, render 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        if request.method== 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            user_obj = authenticate(username=username,password=password)

            if user_obj and user_obj.is_superuser:
                login(request,user_obj)
                return redirect('/dashboard/')
            

            return redirect('/')
        
        return render(request,'login.html')
    
    except Exception as e :
        print(e)


def dashboard(request):
    user_data = User.objects.all()

    
    

    return 



