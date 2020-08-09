from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.views import View, generic

from products.forms import FruitForm
from products.models import Fruit


class ApiFruit(View):

    def get(self, request, *args, **kwargs):
        if len(kwargs) > 0:
            fruit = Fruit.objects.get(pk=kwargs['id'])
            if fruit:
                data = model_to_dict(fruit)
                return JsonResponse(data, safe=False, status=200)
            else:
                return JsonResponse(data={}, safe=False, status=404)
        else:
            fruits = Fruit.objects.all().values('id', 'name', 'price')
            data = list(fruits)
            return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = FruitForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse(data={}, safe=False, status=201)
        else:
            return JsonResponse(data={'errors': dict(form.errors.items())}, safe=False, status=400)

    def delete(self, request, *args, **kwargs):
        print('delete')
        if len(kwargs) > 0:
            fruit = Fruit.objects.get(pk=kwargs['id'])
            if fruit:
                fruit.delete()
                return JsonResponse(data={}, safe=False, status=204)
            else:
                return JsonResponse(data={}, safe=False, status=404)
        else:
            return JsonResponse(data={}, safe=False, status=400)

    def put(self, request, *args, **kwargs):
        print('put')
        print(str(kwargs))
        if len(kwargs) > 0:
            fruit = Fruit.objects.get(pk=kwargs['id'])
            print(str(fruit))
            if fruit:
                print(str(request.POST))
                print(str(request.GET))
                form = FruitForm(request.POST, instance=fruit)
                if form.is_valid():
                    form.save()
                    return JsonResponse(data={}, safe=False, status=204)
                return JsonResponse(data={'errors': dict(form.errors.items())}, safe=False, status=400)
            else:
                return JsonResponse(data={}, safe=False, status=404)
        else:
            return JsonResponse(data={}, safe=False, status=400)

    def patch(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

# JsonResponse(serializers.serialize('json', mensajes), safe=False)