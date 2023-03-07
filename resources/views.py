from django.shortcuts import render
from .models import Resource


def list_resources(request):
    # free_resources = Resource.objects.all()
    free_resources = Resource.objects.all().order_by('-created_at')

    return render(request, 'resources/index.html', {'free_resources': free_resources})
