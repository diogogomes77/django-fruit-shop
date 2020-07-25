from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView


class StaffOnly(FormView):

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden(render(request, "shop/403.html"))
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden(reverse("shop/403.html"))
        return super().post(request, *args, **kwargs)
