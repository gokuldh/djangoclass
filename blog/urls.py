from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

]

## localhost/post/1
## localhost/post/2
## localhost/post/3
## localhost/post/4
