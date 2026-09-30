from django.shortcuts import render
from django.http import HttpResponse
from apps.library.models import BookModel


def index(request):
    books = BookModel.objects.earliest()
    return HttpResponse('Hello')


