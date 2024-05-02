from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import login,authenticate,logout
from rest_framework.viewsets import ViewSet
from rest_framework import generics,status,permissions
from api.serializers import *
from api.models import *
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated

# Create your views here.
class AdminRegistrationView(APIView):
    serializer_class = RegistrationSerializer
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_superuser(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            return Response({'message': 'Admin registered successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminLoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user and user.is_superuser:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message': 'Admin logged in successfully',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DepartmentAPIView(APIView):
     
    permission_classes=[IsAuthenticated]

    def post(self,request,*args,**kwargs):
        serializer=DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class StudProfileAPIView(APIView):
     
    permission_classes=[IsAuthenticated]

    def post(self,request,*args,**kwargs):
        serializer=Stud_Prof_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class StudentListView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, format=None):
        students = Student_Profile.objects.all()
        serializer = Stud_Prof_Serializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Stud_Prof_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Student_Profile.objects.get(pk=pk)
        except Student_Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = Stud_Prof_Serializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = Stud_Prof_Serializer(student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
