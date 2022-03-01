from django.shortcuts import render
from .models import *


def index(request):
    hi = Mcl.objects.all()
    return render(request,'index.html',{"data":hi})
