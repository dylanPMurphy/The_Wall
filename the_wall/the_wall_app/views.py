from django.shortcuts import render, redirect, HttpResponse
from .models import *
from login_reg.models import *
# Create your views here.
def index(request):
        if 'userid' in request.session:
            context ={
                'authenticated_user': User.objects.get(id=request.session['userid']),
                'messages_list': Message.objects.order_by('-created_at'),
                #'comments':Comment.objects.all()
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

def addNewComment(request):
    logged_in_user = User.objects.get(id=request.session['userid'])
    comm = request.POST['comment_content']
    parent = Message.objects.get(id=request.POST['parent_id'])
    Comment.objects.create(message_parent=parent, user_who_commented=logged_in_user, content=comm)
    return redirect('/wall')
    