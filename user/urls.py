from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
     path('', views.index),
     path('signup/', views.signup),
     path('profile/', views.profile),
     path('signin/', views.signin),
     path('signout/',views.signout),
     
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 맨처음 할거
# URL정리

#유저 회원가입/로그인/로그아웃/프로필/프로필 수정
# localhost:8000/user/signup
# localhost:8000/user/signin
# localhost:8000/user/signout
# localhost:8000/user/profile (a.k.a beenzino)
# localhost:8000/user/profile/follow
# * localhost:8000/user/profile/mod

# 메인
# localhost:8000/newsfeed
# localhost:8000/

# 게시글
# localhost:8000/post/posting
# localhost:8000/post/delete
# localhost:8000/post/like
# localhost:8000/post/load


# 댓글
# localhost:8000/comment
# localhost:8000/comment/del
# localhost:8000/comment/mod



# 프로필


# 피드화면
# 글 상세보기
# 글 작성
# 개인 프로필 화면
# 

# user session << 은 좀 그렇고 공부 더 필요
# newsfeed 작업


