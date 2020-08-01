from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.views import View, generic
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


class ApiFruitList(generic.ListView):

    def get(self, request, *args, **kwargs):
        fruits = Fruit.objects.all().values('id', 'name', 'price')
        data = list(fruits)
        # data = core_serializers.serialize("json", fruits)
        return JsonResponse(data, safe=False)
        # return HttpResponse(data, content_type='application/json')


class ApiFruiDetail(generic.DetailView):
    model = Fruit
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        fruit = Fruit.objects.get(pk=kwargs['id'])
        data = model_to_dict(fruit)
        return JsonResponse(data, safe=False)


class ApiFruitCreate(generic.CreateView):
    model = Fruit
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        print('post')
        self.object = None
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        print('get_success_url')
        return reverse_lazy('fruit-api')


class ApiFruit(View):

    def get(self, request, *args, **kwargs):

        if len(kwargs) > 0:
            view = ApiFruiDetail.as_view()
        else:
            view = ApiFruitList.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        view = ApiFruitCreate.as_view()
        return view(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

# JsonResponse(serializers.serialize('json', mensajes), safe=False)