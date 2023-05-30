from django.shortcuts import HttpResponse


def test(request):
    return HttpResponse('<h1>hello</h1>')
