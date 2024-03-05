from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("AAAA32222222321AA2AAAAAAAAAAA")


def get_report(request):
    print(request)
    return HttpResponse("BB3223222222222BBBBBBBBB")