from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PostModel, UserModel
def posting(request):
    if request.method == 'POST':
        username = request.user.username
        my_user = UserModel.objects.get(username=username) # db 에서 가져옴

        # my_tweet = TweetModel.objects.get(id=id)

        ## user 정보 가져와야 함
        my_posting = PostModel()
        print("돌아가라 함수야~~~")
        # user = request.POST.get('username', None)
        user = my_user
        content = request.POST.get('content', None)
        like_count = request.POST.get('like_count', None)

        my_posting.user = my_user
        my_posting.content = content
        
        my_posting.save()
        return HttpResponse(200,"성공") # 200 > 성공했다는 뜻!
        
        

# class PostModel(models.Model):
#     class Meta:
#         db_table = "my_post"
#     user = models.ForeignKey(UserModel, on_delete=models.CASCADE) # 작성자  
#     updated_at = models.DateTimeField(auto_now=True) # 변경 시간
#     content = models.TextField(max_length=500, blank=True) # * status message
#     like_count = models.IntegerField(default=0)
#     create_at = models.DateTimeField(auto_now_add=True)
