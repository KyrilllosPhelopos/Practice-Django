from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK , HTTP_201_CREATED , HTTP_400_BAD_REQUEST
# Create your views here.

class PostView(APIView):
    permission_classes = (AllowAny ,)
    def get(self , request, *args, **kwargs):
        quert_set = Post.objects.all()
        serializer = PostSerializer(quert_set , many = True)
        # if serializer.is_valid() :
        return Response(serializer.data)
    def post(self , request, *args, **kwargs):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=HTTP_200_OK)
        return Response(serializer.errors , status=HTTP_400_BAD_REQUEST)
    
    def put(self , request , pk, *args, **kwargs):
        post = Post.objects.get(pk = pk)
        serializer = PostSerializer(post , data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data , status= HTTP_200_OK)
        return Response(serializer.errors , status= HTTP_400_BAD_REQUEST)
    
    def delete(self , request , pk, *args, **kwargs):
        post = Post.objects.get(pk = pk)
        post.delete() #delete the post 
        return HttpResponse(status = 200)



@csrf_exempt
def Post_List (request):
    if request.method == 'GET':
        query_set = Post.objects.all()
        serializer = PostSerializer(query_set , many =True)
        return JsonResponse(serializer.data , safe=False)
    
    if request.method == 'POST':
        data = JSONParser.parse(request) # to get the data from the request as a JSON
        serializer = PostSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data ,status = 201 )
        return JsonResponse(serializer.errors , status = 400)
    
@csrf_exempt
def Post_Detail(request , pk):
    try:
        post = Post.objects.get(pk = pk)
    except:
        return HttpResponse(status = 404)
    
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = PostSerializer(post , data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status = 201)
        return JsonResponse(serializer.errors , status = 400)
    
    elif request.method == 'DELETE':
        post.delete() #delete the post 
        return HttpResponse(status = 200)



        
