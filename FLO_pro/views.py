from cgitb import text
from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from post.models import PostModel, Comment, UserModel

def newsfeed(request):
    print("함수실행맨")
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
        print("실행")
        user = request.user.is_authenticated
        print("실행2")  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면
            all_newsfeed = PostModel.objects.all().order_by('-create_at')
            # for newsfeed in all_newsfeed:
            #     print(newsfeed.comment_set.all())
            # return render(request, 'main.html/', {'newsfeeds':all_newsfeed}) # list 
            print("asdfasdf")
            new_all_newsfeed = []
            for newsfeed in all_newsfeed:
                reply = Comment.objects.filter(post = newsfeed).order_by('-create_at')
                for i in reply:
                    i = i.text
                
                print(newsfeed.user.username)
                new_all_newsfeed.append(dict(
                    new_id = newsfeed.id,
                    new_user = newsfeed.user,
                    new_reply = reply,
                    new_image = newsfeed.image,
                    new_content = newsfeed.content,
                    new_likes = newsfeed.likes,
                ))

            all_user = UserModel.objects.all().exclude(id=request.user.id) 
            print(all_user)
                
                
                
            return render(request, 'main.html/', {'newsfeeds': new_all_newsfeed,'all_users':all_user}) # list 
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

def test(request):
    print("팔로우 테스트 페이지")
    user_follow = request.user
    user_list = UserModel.objects.all().exclude(username=request.user.username)
    return render(request,'user/user_list.html',{'user_list':user_list})