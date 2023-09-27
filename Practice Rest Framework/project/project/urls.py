"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1.views import (PostView , Post_Detail , Post_List , PostMixinListView ,
                         PostListView ,PostDestroyView, PostRetrieveView , OwnerRetrieveView , 
                         CommentRetrieveView ,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    #path('api/posts/<int:pk>/', PostView.as_view() , name = 'post_list'),
    # path('api/posts/', PostView.as_view() , name = 'post_list'),
    # path('api/post-list/' , Post_List , name = 'Post_List' ),
    # path('api/posts/<int:pk>/',Post_Detail , name  ='Post_Detail'),

    # path('api/posts/' , PostMixinListView.as_view() , name = 'PostMixinListView' ),
    # path('api/posts/' , PostListView.as_view() , name = 'PostListView' ),
    # path('api/posts/<int:pk>/',PostRetrieveView.as_view()  , name  ='PostRetrieveView'),
    path('api/owners/<int:pk>/',OwnerRetrieveView.as_view()  , name  ='Owner_RetrieveView'),
    path('api/comments/<int:pk>/',CommentRetrieveView.as_view()  , name  ='Comment_RetrieveView'),
    # path('api/posts/<int:pk>/delete',PostDestroyView.as_view()  , name  ='PostDestroyView'),

    path('api/' , include('app1.urls'))


]
