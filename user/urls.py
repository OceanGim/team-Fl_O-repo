from django.urls import path
from . import views

urlpatterns =[
     path('', views.index),
     path('signup/', views.signup),
     path('profile/', views.profile),
     path('signin/', views.signin),
    
]

# url 정리하기
# index, profile 위치 이동
# profile app 만들어서 이동
# index 이동
# index FLO_pro 로 이동
# index 에 들어갔을 때, session 있으면 메인페이지로 
# session 이 없으면 signin 페이지로