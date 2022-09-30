from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    me = request.user.is_authenticated
    print("안녕하세요")
    if me:
        return redirect('/')
    else:
        return render(request, '/user/signin.html/')

def main(request):
    return render(request, 'user/signin.html/') # 로그인