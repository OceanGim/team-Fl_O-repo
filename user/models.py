from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    updated_at = models.DateTimeField(auto_now=True) # 변경 시간
    bio = models.TextField(max_length=500, blank=True) # * status message
    image = models.TextField(max_length=500, blank=True, default = 'default_image.jpg') # * profile image
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followee')

# idc
# from_user_id 얘가
# to_user_id 얘를 팔로우 한다



# todo follow following user.following 
# ^ 내가 유저를 참조하면 팔로잉
# ^ 다른 유저가 나를 참조하면 팔로우
    
# 팔로우 창
# 팔로워 창