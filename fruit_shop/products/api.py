from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product, Fruit


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'


class ApiFruitList(APIView):

    def get(self, request):
        fruits = Fruit.objects.all()
        serialized = FruitSerializer(fruits, many=True)
        return Response(serialized.data)

