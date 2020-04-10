from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Offer

# Create your views here.
@login_required(login_url='/login/')
def viewOffer(request):
    offers = Offer.objects.all()

    return render(request, 'offers.html', {'offers': offers})
