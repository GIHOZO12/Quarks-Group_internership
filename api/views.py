from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import uuid

users={}

class CreateUserView(APIView):
    def post(self,request):
        name=request.data.get("name")
        email=request.data.get("email")
        if not name or not email:
            return Response({"error":"Please provide name and email to proceed"},status=400)
        user_id=str(uuid.uuid4())
        users[user_id]={"name":name,"email":email}
        return Response({"user_id":user_id},status=201)

class GetUserView(APIView):
    def get(self,request,user_id):
        user=users.get(user_id)
        if not user:
            return Response({"error":"User not found"},status=404)
        return Response(user,status=200)