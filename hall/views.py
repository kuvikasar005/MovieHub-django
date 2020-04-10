from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .filters import HallFilter

from .models import Hall

# Create your views here.
@login_required(login_url='/login/')
def viewHall(request):
    halls = Hall.objects.all()

    hallFilter = HallFilter(request.GET, queryset=halls)
    halls = hallFilter.qs

    return render(request, 'viewHall.html', {'halls': halls, 'hallFilter': hallFilter})
