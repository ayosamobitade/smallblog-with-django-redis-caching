from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, View
from .models import *

# Create your views here.

class bloggyView(ListView):
    queryset = phone.objects.all()
    context_object_name = "phones"
    template_name = "bloggy/bloggy.html"


class phoneView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello here, you're welcome")

