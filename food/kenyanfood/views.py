from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Food
from .serializer import FoodSerializer

# Create your views here.
@api_view(['GET'])
def getFood(request):
    """Get food from the api"""

    food = Food.objects.all()
    serializer = FoodSerializer(food, many=True)
    return Response(serializer.data)