from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    updated_at = models.DateTimeField(auto_now=True) # 변경 시간
    bio = models.TextField(max_length=500, blank=True) # * status message