from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import UserModel
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

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

def profile(request):
    return render(request, 'content/profile.html/') # 프로필