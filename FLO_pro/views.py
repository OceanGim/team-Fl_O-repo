from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from post.models import PostModel

def newsfeed(request):
    print("함수실행맨")
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면
            all_newsfeed = PostModel.objects.all().order_by('-create_at')
            return render(request, 'main.html/', {'newsfeeds': all_newsfeed}) # list 
        else:  # 로그인이 되어 있지 않다면
            return redirect('/user/signin/')

def main(request):
    #* 로그인 체크
    user = request.user.is_authenticated
    print("안녕하세요")
    if user: # 로그인 상태 : newsfeed 페이지 이동
        print("유저 있음")
        return redirect('/newsfeed/') # 127.0.0.1:8000/newsfeed
    else: # 로그아웃 상태 : signin 페이지로 이동
        print("로그아웃 상태")
        return redirect('/user/signin/')

# localhost:8000/ 이걸 입력하면 main함수를 실행함