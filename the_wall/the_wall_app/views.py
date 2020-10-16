from django.shortcuts import render
from .models import *
from login_reg.models import *
# Create your views here.
def index(request):
    context ={
        'authenticated_user': User.objects.get(id=request.session['userid'])
    }
    print(request.session)
    print(request.session['userid'])
    return render(request, 'wall.html', context)