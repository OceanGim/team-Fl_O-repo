from django.db import models
from user.models import UserModel
from django.conf import settings

class PostModel(models.Model):
    class Meta:
        db_table = "my_post"
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE) # 작성자  
    updated_at = models.DateTimeField(auto_now=True) # 변경 시간
    content = models.TextField(max_length=500, blank=True) # * status message
    like_count = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    image = models.TextField(max_length=500, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like', blank = True)


class Comment(models.Model):
    class Meta:
        db_table = "user_comment"
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    comment_user = models.ForeignKey(UserModel, on_delete=models.CASCADE) # 작성자 
    text = models.TextField(max_length = 300) #댓글 내용
    create_at = models.DateTimeField(auto_now_add=True) # 생성 시간    


