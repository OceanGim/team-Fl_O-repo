from django.db import models

# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table = "my_user"

    email = models.CharField(max_length=20, null=False) # 아이디로 쓰여질 email
    username = models.CharField(max_length=20, null=False) # 실명
    nickname = models.CharField(max_length=20, null=False) # 별명
    password = models.CharField(max_length=256, null=False) # 비밀번호
    created_at = models.DateTimeField(auto_now_add=True) # 생성 시간
    updated_at = models.DateTimeField(auto_now=True) # 변경 시간