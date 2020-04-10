from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ticket.models import Ticket

# Create your views here.
@login_required(login_url='/login/')
def bookHistory(request):
    tickets = Ticket.objects.filter(user__username=request.user)
    return render(request, 'bookHistory.html', {'tickets':tickets})
