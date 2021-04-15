from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from .tables import *
from django.db import connection
# Create your views here.

def show_map(request):
    """
    map
    """
    qs = Squirrel.objects.all()[:100]
    return render(request, 'squirrel/map.html', {'qs': qs})

def sightings_list(request):
    """
    sightings
    """
    qs = Squirrel.objects.all()
    table = SquirrelTable(qs)
    table.paginate(page=request.GET.get("page", 1), per_page=50)
    return render(request, 'squirrel/list.html', {'table': table})

