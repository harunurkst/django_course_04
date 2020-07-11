from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request, name, roll):
    str = "Hello {}, How are you".format(name)
    return HttpResponse(str)


def summation(request, a, b):
    print(type(a))
    s = a + b
    s = "<h1>Hello How are you? </h1>"
    return HttpResponse(s)


def home(request):
    context = {
        'students': range(1, 50)
    }

    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')





