# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from .forms import New_User

# Create your views here.
def index(request):
    all_users = User.objects.all()
    return render(request, 'index.html', { 'all_users': all_users})
def new(request):
    request.session.clear()
    form = New_User()
    return render(request, 'new.html', {'form': form})
def create(request):
    form = New_User(request.POST)
    if form.is_valid():
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            request.session['errors'] = errors
            print errors
            return redirect('/new')
        else:
            f_name = request.POST['first_name']
            l_name = request.POST['last_name']
            e_mail = request.POST['email']
            new_user = User.objects.create(first_name=f_name, last_name=l_name, email=e_mail)
            new_user.save()
            request.session.clear()
            return redirect('/')
    else:
        print 'not valid'
        return redirect('/new')
def show(request, id):
    request.session.clear()
    user = User.objects.get(id=id)
    return render(request, 'user.html', {'data': user})
def edit(request, id):
    request.session.clear()
    user = User.objects.get(id=id)
    return render(request, 'edit.html', {'data': user})
def update(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        new_errors = []
        for error in errors:
            new_errors.append(error)
        request.session['errors'] = new_errors
        return redirect('/')
    else:
        id = request.POST['id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        User.objects.filter(id=id).update(first_name=first_name, last_name=last_name, email=email)
        return redirect('/')
def destroy(request, id):
    User.objects.filter(id=id).delete()
    return redirect('/')