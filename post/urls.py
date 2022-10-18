
from django.urls import path, include
from . import views
from django.urls import path
from .views import Main, UploadFeed
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', Main.as_view()),
    path('posting/', views.posting),
    path('comment/', views.comment),
    path('like/<int:id>', views.post_like, name='post_like'),
    # path('favorite/<int:id>', views.post_favorite, name='post_favorite'),    
    path('delete/<int:id>', views.delete_post, name='delete_post'),
] 