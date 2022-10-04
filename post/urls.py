
from django.urls import path, include
from . import views
from django.urls import path
from .views import Main, UploadFeed
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', Main.as_view()),
    path('posting/', views.posting),
    path('like/<int:id>', views.post_like, name='post_like'),
    path('delete/<int:id>', views.delete_post, name='delete_post'),
] 
