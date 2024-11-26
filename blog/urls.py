from . import views
# self added
from django.urls import path
from blog import views
urlpatterns = [
    path('posts/', views.MyPostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
