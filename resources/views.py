from django.shortcuts import render
from .models import Resource
from django.contrib.auth.decorators import login_required


@login_required
def list_resources(request):
    # free_resources = Resource.objects.all()
    free_resources = Resource.objects.all().order_by('-created_at')
    for thing in free_resources:
        print(free_resources)

    return render(request, 'resources/index.html', {'free_resources': free_resources})
