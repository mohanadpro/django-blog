from . import views
# self added
from django.urls import path
urlpatterns = [
    path('', views.about_me, name='about'),
]
