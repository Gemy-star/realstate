from django.shortcuts import render
from . import models


def all_projects(request):
    proj = models.Location.objects.all()
    return render(request, 'realstate/projects.html', context={"projects": proj})


def all_state(request, pk):
    states = models.ProjectState.objects.filter(location__projectstate__developer_id=pk)
    return render(request, 'realstate/states.html', context={"states": states})


def all_state_developer(request, pk):
    states = models.ProjectState.objects.filter(developer__projectstate__developer_id=pk)
    return render(request, 'realstate/states.html', context={"states": states})
