from django.contrib import admin
from .models import PostModel
from .models import Comment

# Register your models here.
admin.site.register(PostModel)
admin.site.register(Comment)