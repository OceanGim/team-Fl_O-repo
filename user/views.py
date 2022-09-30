from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import UserModel


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
        nickname = request.POST.get('nickname', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        if password != password2:
            # 패스워드 다릅니다 출력 messages 프레임워크 후에 작업 예정
            # 패스워드만 비우기 기능
            return redirect('/signup/')
        else:
            exist_user = UserModel.objects.filter(email=email)
            
            if exist_user:
                # print("아이디가 이미 존재합니다!!!!!!!!!!!!!!!!!")
                messages = {'message' : "아이디 다시 쓰지마라...."}
                return render(request, 'user/signup.html',messages)
            else:
                new_user = UserModel()
                new_user.email = email
                new_user.username = username
                new_user.nickname = nickname
                new_user.password = password
                new_user.save()
                return redirect('/')  # 여기서 로그인페이지로 넘어감! 조심조심!! 주소를 써야하는데 singup으로 되어있
                # singin page로 넘어가면서 가입이 완료됐습니다. 이메일은 :~~@~~~.~~~ 입니다 메시지 출력
      
                
def signin(request):
    if request.method == 'POST':
        print("signin method post")
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        print(email,password)
        
        me = UserModel.objects.get(email=email) # 사용자 불러오기
        if me.password == password: # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            request.session['user'] = me.email # 세션에 사용자 이름 저장#
            return render(request,'index.html/')
        else:
            return redirect('/signin')
    elif request.method == 'GET':
        return render(request, 'user/signin.html')

        
        
def index(request):
    return render(request, 'index.html/') # 메인페이지

def profile(request):
    return render(request, 'content/profile.html/') # 프로필