from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register("posts", PostViewSet) # have all the http methods 
post_details = PostViewSet.as_view({
    'get' : 'list',
    'post' : 'create'}
)

urlpatterns = [
    path('', include(router.urls)),
    path('custom/', post_details , name = 'custom' )
]