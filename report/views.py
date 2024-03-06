from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("index")


def get_report(request):
    print(request)
    return render(request, 'report.html')