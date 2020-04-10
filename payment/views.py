from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from shows.models import Show

# Create your views here.
@login_required(login_url='/login/')
def orderSummary(request):
    show = Show.objects.get(id=request.POST["showId"])
    seats = int(request.POST["numofseat"])
    amount = int(show.price) * seats
    seatsAvailable = int(show.seats)
    path = request.POST["path"]

    if seats <= seatsAvailable:
        return render(request, 'orderSummary.html', {'show':show,"seats":seats, 'amount':amount})
    else:
        msg="Sorry, We only have " + str(seatsAvailable) + " seats left."
        messages.info(request, msg)
        return redirect(path)

@login_required(login_url='/login/')
def payment(request):
    showId = request.POST["showId"]
    amount = request.POST["amount"]
    seats = request.POST["seats"]

    context = {'showId':showId, 'amount': amount, 'seats': seats}

    return render(request, 'payment.html', context)
