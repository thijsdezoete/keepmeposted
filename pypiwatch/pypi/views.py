from django.shortcuts import render_to_response
from .models import Package, Watcher

# Create your views here.
def index(request):
    watchers = Watcher.objects.all()[:10]
    print watchers
    return render_to_response(
            'index.html', 
            {'watchers': watchers},
    )
    
