from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def newsfeed(request):
    return render(request, "main.html")

def main(request):
    #* 로그인 체크
    user = request.user.is_authenticated
    print("안녕하세요")
    if user: # 로그인 상태 : newsfeed 페이지 이동
        print("유저 있음")
        return redirect('/newsfeed/')
    else: # 로그아웃 상태 : signin 페이지로 이동
        print("로그아웃 상태")
        return redirect('/user/signin/')

# localhost:8000/ 이걸 입력하면 main함수를 실행함