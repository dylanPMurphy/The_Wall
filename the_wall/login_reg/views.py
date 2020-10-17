from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages
# Create your views here.

def index(request):

    return render(request, 'index.html')

def register(request):
    if request.method =="POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            
            
            # include some logic to validate user input before adding them to the database!
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
            print(pw_hash)      # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'    
            
            # be sure you set up your database so it can store password hashes this long (60 characters)
            # make sure you put the hashed password in the database, not the one from the form!
            newUser = User.objects.create(name=request.POST['user_name'], password=pw_hash, email=request.POST['email'])
            request.session['userid'] = newUser.id
            return redirect('/wall') 
            #Create an account

def reg_success(request):
    return render(request, 'successful_REG.html')


def login(request):
    if request.method =="POST":
        user = User.objects.filter(name=request.POST['login_uname']) # why are we using filter here instead of get?
        if user and request.POST['login_pass']: # note that we take advantage of truthiness here: an empty list will return false
            logged_user = user[0] 
            # assuming we only have one user with this username, the user would be first in the list we get back
            # of course, we should have some logic to prevent duplicates of usernames when we create users
            # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
            if bcrypt.checkpw(request.POST['login_pass'].encode(), logged_user.password.encode()):
                # if we get True after checking the password, we may put the user id in session
                request.session['userid'] = logged_user.id
                # never render on a post, always redirect!
                return redirect('/wall')
            else:
                messages.error(request, "Username or password incorrect")
                return redirect('/')
        else:
            messages.error(request, "Username or password incorrect")
            return redirect('/')

def success(request):

    context = {
        'session_user':User.objects.get(id=request.session['userid'])
    }
    return render(request, 'successful_LOGIN.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')