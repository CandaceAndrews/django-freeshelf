from django.shortcuts import render


def list_resources(request):
    return render(request, 'books/index.html')
