from rest_framework import viewsets
from .models import Product, Order, Review
from .serializers import ProductSerializer, OrderSerializer, ReviewSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RegisterView(APIView):
    def post(self, request):
        user = User.objects.create_user(
            username=request.data['username'],
            email=request.data['email'],
            password=request.data['password']
        )
        return Response({'status': 'User created'}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            login(request, user)
            return Response({'status': 'User logged in'})
        return Response({'status': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
