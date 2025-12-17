from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()

    data = []
    for p in products:
        data.append({
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "description": p.description,
            "category": p.category,
            "stock": p.stock,
            "image": request.build_absolute_uri(p.image.url) if p.image else None
        })

    return Response(data)
@api_view(['GET'])
def product_detail(request, id):
    try:
        p = Product.objects.get(id=id)
        data = {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "description": p.description,
            "category": p.category,
            "stock": p.stock,
            "image": request.build_absolute_uri(p.image.url) if p.image else None
        }
        return Response(data)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)
    

@api_view(['POST'])
def register_user(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')

    if User.objects.filter(username=email).exists():
        return Response(
            {"error": "Email already exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(
        username=email,
        email=email,
        password=password,
        first_name=name
    )

    return Response(
        {"message": "User created successfully"},
        status=status.HTTP_201_CREATED
    )


from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            "message": "Login successful",
            "user": {
                "name":user.first_name,
                "email":user.email
            },
            "token": {
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }
        })
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
