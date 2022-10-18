from unittest.mock import patch
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from .models import PostModel, UserModel
from rest_framework.views import APIView
from post.models import PostModel, Comment
from rest_framework.response import Response
import os
from FLO_pro.settings import MEDIA_ROOT
from uuid import uuid4 
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .import models
from django.views.generic.base import View
from urllib.parse import urlparse


class Main(APIView):
    def get(self, request):
        feed_list = PostModel.objects.all().order_by('-id')
        return render(request, 'user/main.html', context=dict(feed_list=feed_list))


class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        content = request.data.get('content')
        image = uuid_name
        profile_image = request.data.get('profile_image')
        user_id = request.data.get('user_id')

        PostModel.objects.create(content=content, image=image, profile_image=profile_image, user_id=user_id, like_count=0)

        return Response(status=200)

        
def posting(request):
    if request.method == 'POST':

        print("posting method POST")
        username = request.user.username
        my_user = UserModel.objects.get(username=username) # db 에서 가져옴

        file = request.FILES['file']
        uuid_name = uuid4().hex # 자동생성
        save_path = os.path.join(MEDIA_ROOT, uuid_name) # 저장 경로
        with open(save_path, 'wb+') as destination: # 저장과정 ?
            for chunk in file.chunks():
                destination.write(chunk)
        content = request.POST.get('content', None)
        image = uuid_name # 사진 이름 (28918374919.jpg)
        print(image)

        PostModel.objects.create(content=content, image=image, user=my_user)
        return HttpResponse(200, "성공")



def comment(request):

    if request.method == 'POST':
        username = request.user.username
        my_comment = Comment()
        a = request.POST.get('newsfeed_new_id','')
        my_comment.post = PostModel.objects.get(id = a)
        my_comment.comment_user = UserModel.objects.get(username = username)
        print("Comment regeister")
        my_comment.text = request.POST.get('my-comment','')
        my_comment.save()
        return redirect('/')
        
#글 삭제하기
@login_required
def delete_post(request, id):
    print("글 삭제 들어옴")
    my_tweet = PostModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/')


#좋아요
@login_required
def post_like(request, id):
    print("post like들어옴")
    me = request.user
    click_post = PostModel.objects.get(id=id) #클릭된 유저
    if me in click_post.likes.all(): #라이크 한 사람들 모두 가져옴
        click_post.likes.remove(request.user) # 그 사람중에 나를 뺌
    else:
        click_post.likes.add(request.user)
    return redirect('/')

# class post_like(View):
#     def get(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return HttpResponseForbidden()
#         else:
#             if 'post_id' in kwargs:
#                 post_id = kwargs['post_id']
#                 post = PostModel.objects.get(pk=post_id)
#                 user = request.user
#                 if user in post.like.all():
#                     post.like.remove(user)
#                 else:
#                     post.like.add(user)
#             referer_url = request.META.get('HTTP_REFERER')
#             path = urlparse(referer_url).path
#             return HttpResponseRedirect(path)

              
# class post_favorite(View): 
#   def get(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return HttpResponseForbidden()
#         if 'post_id' in kwargs:
#                 post_id = kwargs['post_id']
#                 post = PostModel.objects.get(pk=post_id)
#                 user = request.user
#                 if user in post.favorite.all():
#                     post.favorite.remove(user)
#                 else:
#                     post.favorite.add(user)
#                     return HttpResponseRedirect('/')
                    

