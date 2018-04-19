
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime
import random
from .models import User

# Create your views here.

def index(request):
     
    # print Danny
    if 'friend' not in request.session:
        friend_id = 0
        friends_set = []
        enemies_set = []

    else:
        friend_id = request.session['friend']
        this_user = User.objects.get(id=friend_id)
        friends_set = this_user.get_friends().exclude(id=friend_id)
        enemies_set = set(User.objects.exclude(id=friend_id)).difference(this_user.get_friends())
    
    # print '8'*50
    # print User.objects.all()
    # print User.objects.get_friends(this_user)
    # print '8'*50
       
     
    context = {
        "friends":User.objects.all(),
        "friends_list": friends_set,
        "enemies_list":enemies_set
    }

    return render(request, 'user_friend_app/index.html', context)

def add(request):
    User.objects.create(name=request.POST['name'])
    return redirect('/')

def makefriend(request):
    person1 = User.objects.get(id=request.POST['friend_1'])
    person2 = User.objects.get(id=request.POST['friend_2'])
    person1.add_friendship(person2)
    return redirect('/')

def currentfriend(request):
    print request.POST['friend']
    print User.objects.get(id=request.POST['friend']).id
    request.session['friend'] = User.objects.get(id=request.POST['friend']).id
    return redirect('/')
    

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def goHome(request):
    return redirect('/')

def showall(request):
    context = {
        'db_dump' : User.objects.all()
    }
    return render(request, 'user_friend_app/showall.html',context)