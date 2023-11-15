from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    """Serializing the Food model(Ikr!!)"""

    class Meta:
        model=Food
        fields=('name', 'description')