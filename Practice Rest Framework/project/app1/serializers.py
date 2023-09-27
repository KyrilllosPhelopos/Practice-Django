from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post , Comment

User = get_user_model()

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' , 'username')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id' , 'title')
class PostSerializer(serializers.ModelSerializer):
    
    owner = serializers.HyperlinkedIdentityField(many = False ,view_name = 'Owner_RetrieveView') # to link the owner field with  a user to appear as alink
    comments = serializers.HyperlinkedRelatedField(queryset = Comment.objects.all() , many = True , view_name= 'Comment_RetrieveView') 
    class Meta:
        model = Post
        fields = (
            'title',
            'owner',
            'custom_id',
            'category',
            'publish_date',
            'last_updated',
            'comments',
        )