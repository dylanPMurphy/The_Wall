from django.shortcuts import render, HttpResponse
from .models import *
from login_reg.models import *
# Create your views here.
def index(request):
        if 'userid' in request.session:
            context ={
                'authenticated_user': User.objects.get(id=request.session['userid'])
            }
            print(request.session)
            print(request.session['userid'])
            return render(request, 'wall.html', context)
        else:
            return HttpResponse("ERROR NOT SIGNED IN")