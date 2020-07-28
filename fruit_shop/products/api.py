from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers as core_serializers

from products.models import Fruit


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'


class DrfFruitList(APIView):

    def get(self, request):
        fruits = Fruit.objects.all()
        serialized = FruitSerializer(fruits, many=True)
        return Response(serialized.data)


class ApiFruitList(View):

    def get(self, request):
        fruits = Fruit.objects.all().values('id', 'name', 'price')
        data = list(fruits)
        #data = core_serializers.serialize("json", fruits)
        return JsonResponse(data, safe=False)
        #return HttpResponse(data, content_type='application/json')

# JsonResponse(serializers.serialize('json', mensajes), safe=False)