from django.shortcuts import render
from .forms import SigninForm
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == "GET":
        return render(request, 'login/signup.html', {'f':SigninForm()})
    elif request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                new_user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['password'])
                new_user.save()
                return HttpResponseRedirect(reverse('votd:index'))
            else:
                return render(request, 'login/signup.html',{'f':form, 'error':'비밀번호와 비밀번호 확인이 일치하지 않습니다.'})
        else:
            return render(request, 'login/signup.html',{'f':form})


def signin(request):
    if request.method == "GET":
        return render(request, 'login/signin.html', {'f':SigninForm()} )
    elif request.method == "POST":
        form = SigninForm(request.POST)
        id = request.POST['username']
        pw = request.POST['password']
        u = authenticate(username=id, password=pw)

        if u: 
            login(request, user=u) 
            return HttpResponseRedirect(reverse('vote:index'))
        else:
            return render(request, 'login/signin.html',{'f':form, 'error':'아이디나 비밀번호가 일치하지 않습니다.'})
    
from django.contrib.auth import logout 

def signout(request): 
    logout(request)
    return HttpResponseRedirect(reverse('vote:index'))