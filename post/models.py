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
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like')

# class Like(models.Model):
#     user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like')
#     post = models.ForeignKey(PostModel, on_delete=models.CASCADE)


# 이미지 파일 >>>>> 이미지파일을 media에 저장 저장시 이름을 uuid.hex << 이름을 바꿔줌 저장 >> db 이름저장 
# 불러올때, uuidname 오겠죠? 이이름으로 media에서 찾는거에요 



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

