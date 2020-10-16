from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    context ={
        'authenticated_user': User.objects.get(id=request.session['userid'])
        
    }
    return render(request, 'wall.html')