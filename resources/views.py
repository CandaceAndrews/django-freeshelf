from django.shortcuts import render, get_object_or_404
from .models import Resource
from django.contrib.auth.decorators import login_required


@login_required
def list_resources(request):
    # free_resources = Resource.objects.all()
    free_resources = Resource.objects.all().order_by('-created_at')
    for thing in free_resources:
        print(free_resources)

    return render(request, 'resources/index.html', {'free_resources': free_resources})


def details_about_resource(request, pk):
    resource_description = get_object_or_404(Resource, pk=pk)
    return render(request, 'resources/details_about_resource.html', {'resource_description': resource_description})
