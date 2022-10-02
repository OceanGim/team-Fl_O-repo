from django.db import models
from user.models import UserModel

class PostModel(models.Model):
    class Meta:
        db_table = "my_post"
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE) # 작성자  
    updated_at = models.DateTimeField(auto_now=True) # 변경 시간
    content = models.TextField(max_length=500, blank=True) # * status message
    like_count = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)





# 글쓴이
# 내용
# 수정시간
# 만든 시간
# 좋아요 수 기본 0
# 댓글 << 강의 에서 어떻게한지 아시는분

# Create your models here.
# class TweetModel(models.Model):
#     class Meta:
#         db_table = "tweet"

#     author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
#     content = models.CharField(max_length=256)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class TweetComment(models.Model):
#     class Meta:
#         db_table = "comment"
#     tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
#     author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
#     comment = models.CharField(max_length=256)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

