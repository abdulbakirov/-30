
from django.shortcuts import render



def index(request):
    return render(request, 'main/index.html')


def test(request):
    return render('зайбал чктыго жетим ')