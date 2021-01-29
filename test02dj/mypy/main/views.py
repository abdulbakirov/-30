
from django.shortcuts import render



def index(request):
    return render(request, 'main/index.html')


def test(request):
    return render(request, 'main/test.html')

def test01(request):
    return render(request, 'main/test01.html')