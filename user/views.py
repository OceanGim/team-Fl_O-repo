from django.shortcuts import render, redirect, HttpResponse
from .models import UserModel
from post.models import PostModel
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from FLO_pro.settings import MEDIA_ROOT
from uuid import uuid4 
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.response import Response

import pprint


def main(request):
    return render(request, 'user/signin.html/') # 로그인

def signup(request):
    print("signup 들어옴")
    if request.method == 'GET': # GET 메서드로 요청이 들어올 경우        
        print("signup get method")
        return render(request, 'user/signup.html/')
    elif request.method == 'POST': # POST 메서드로 요청이 들어올 경우
        print("signup post method")
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        firstname = request.POST.get('firstname', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        if password != password2:
            # 패스워드 다릅니다 출력 messages 프레임워크 후에 작업 예정
            # 패스워드만 비우기 기능
            print("패스워드 다름")
            return redirect('/user/signup/')
        else:
            exist_user = UserModel.objects.filter(username=username)
            
            if exist_user:
                # print("아이디가 이미 존재합니다!!!!!!!!!!!!!!!!!")
                messages = {'message' : "아이디를 다시 입력해주세요."}
                return render(request, 'user/signup.html',messages)
            else:
                print(firstname)
                UserModel.objects.create_user(username=username,password=password,email = email,first_name = firstname)

                return redirect('/')  # 여기서 로그인페이지로 넘어감! 조심조심!! 주소를 써야하는데 singup으로 되어있
                # * singin page로 넘어가면서 가입이 완료됐습니다. 이메일은 :~~@~~~.~~~ 입니다 메시지 출력
      
                
def signin(request):
    if request.method == 'POST':
        print("signin method post")
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username,password)
        
        # 로그인 인증
        me = auth.authenticate(request, username=username, password=password) #* db에 username, password 있느냐?
        print(type(me))
        # me = UserModel.objects.get(username=username) # 사용자 불러오기
        if me is not None: # *저장된 사용자의 패스워드와 입력받은 패스워드 비교
            print("로그인 성공!!")
            auth.login(request,me) # session
            return redirect('/') # index.html로 들어갑니다.
        else:
            print("로그인 실패!")
            return redirect('/user/signin')
    elif request.method == 'GET':
        return render(request, 'user/signin.html')
        
@login_required
def signout(request):
    auth.logout(request) # 로그아웃 session 종료
    return redirect('/') # logout 버튼을 누르면 index.html로 이동한다.
        
        
def index(request):
    return render(request, 'index.html/') # 메인페이지

@csrf_exempt
def profile(request):
    print("views.profile 들어옴")

    # GET 장고에서 웹으로 정보를 보낸다
    if request.method == 'GET': # GET 메서드로 요청이 들어올 경우        
        print("profile get mehtod")
        user = request.user.is_authenticated
        my_user = request.user
        if user:  # 로그인 한 사용자라면
            user_profile = UserModel.objects.get(username=my_user.username)
            print(f"{user_profile.id}, {user_profile.username}, {user_profile.image}")
            post_profile = PostModel.objects.filter(user_id=user_profile).order_by('-create_at')
            return render(request, 'user/profile.html/', {'profiles': user_profile, 'postprofiles':post_profile}) # list
        else:  # 로그인이 되어 있지 않다면
            return redirect('/user/profile/')
    
    # POST 웹에서 정보를 받는다
    elif request.method == 'POST':
        print("profile_register")
        file = request.FILES['file']
        uuid_name = uuid4().hex # 자동생성
        save_path = os.path.join(MEDIA_ROOT, uuid_name) # 저장 경로
        with open(save_path, 'wb+') as destination: # 저장과정 ?
            for chunk in file.chunks():
                destination.write(chunk)
        update_image = uuid_name # 사진 이름 (28918374919.jpg)
        print(update_image)
        # 이미 있는 유저에다가 image 만 교체  :  나(본인)  세션
        my_user = request.user
        my_profileimg = UserModel.objects.get(username=my_user.username) 
        print('photo print')
        print(f"{my_profileimg.id}, {my_profileimg.username}, {my_profileimg.image}")
        my_profileimg.image = update_image
        my_profileimg.save()
        # save()
        print(f"{my_profileimg.id}, {my_profileimg.username}, {my_profileimg.image}")
        # my_profileimg = id = aaa pw = 111 image = 28938490184 email = a@aa
        # return HttpResponse("성공",status=200) # url 주소 127.0.0.1/8000'/user/profile/'
        # return Response(status=200, data=dict(message="프로필사진 변경 성공!"))
        return HttpResponse(200, "성공")

# OOO = UserModel.objects.all() # 업데이트 할 데이터 가져오기
# OOO.update(title='test title') 

@login_required
def user_view(request, id):
    if request.method == 'GET':
        get_user = UserModel.objects.get(id = id)
        post_profile = PostModel.objects.filter(user_id=id).order_by('-create_at')
        return render(request,'user/user_profile.html' , {'get_user' : get_user, 'postprofiles':post_profile})
    else:
        pass
        
        
       # 1. 클릭한 유저 찾기 
       # 2. 그 정보 html에 넣기

def follow(request,id):
    print("follow 들어옴")
    me = request.user
    target_user = UserModel.objects.get(id=id) #클릭된 유저
    if me in target_user.follow.all(): #라이크 한 사람들 모두 가져옴
        target_user.follow.remove(request.user) # 그 사람중에 나를 뺌
    else:
        target_user.follow.add(request.user)
    return redirect('/user/profile/'+str(id))
       