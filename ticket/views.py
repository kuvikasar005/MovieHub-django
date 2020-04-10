from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

from shows.models import Show
from .models import Ticket

# Create your views here.
@login_required(login_url='/login/')
def bookTicket(request):
    showId = request.POST["showId"]
    seats = request.POST["seats"]
    amount = request.POST["amount"]

    method = "Credit Card"

    user = User.objects.get(username=request.user)
    show = Show.objects.get(id=showId)

    # print(seats)
    # print(amount)
    # print(user)
    # print(show)

    ticket = Ticket(user=user, show=show, seats=seats, amount=amount, method=method)
    ticket.save()

    print("before - ", show.seats)
    show.seats = show.seats - int(seats)
    show.save()
    print("after - ", show.seats)

    id = ticket.id

    #send send_mail

    subject = "MovieHub Ticket Booked"

    message = "Hello " + str(user.first_name).upper() + ",\n\nYour Ticket for the show " + str(show) + " is successfully Booked. Your Ticket id is " + str(id) + " . Please carry a screenshot of this mail and show it when asked for confirmation. \n\nPlease enjoy your movie and visit our site again. Thank You;) \n\n Regards, \n MovieHub"
    # print(message)

    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    return render(request, 'bookSuccess.html', {'id': id})
