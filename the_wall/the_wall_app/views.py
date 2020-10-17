from django.shortcuts import render, redirect, HttpResponse
from .models import *
from login_reg.models import *
# Create your views here.
def index(request):
        if 'userid' in request.session:
            context ={
                'authenticated_user': User.objects.get(id=request.session['userid']),
                'messages_list': Message.objects.all()
            }
            print(request.session)
            print(request.session['userid'])
            return render(request, 'wall.html', context)
        else:
            return HttpResponse("ERROR NOT SIGNED IN")

def addNewMessage(request):
    logged_in_user = User.objects.get(id=request.session['userid'])
    mess = request.POST['message_content']
    Message.objects.create(user_who_posted=logged_in_user, content=mess)
    return redirect('/wall')