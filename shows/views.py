from django.shortcuts import render
from .models import Show
from datetime import date,timedelta
from django.contrib.auth.decorators import login_required
from .filters import ShowFilter

# Create your views here.
@login_required(login_url='/login/')
def viewShows(request, movie):
        shows = Show.objects.filter(movie__name=movie)
        print("before search - ", shows)

        movie = movie

        showFilter = ShowFilter(request.GET, queryset=shows)
        shows = showFilter.qs
        print("after search - ", shows)

        if request.POST.get("hall", '') != '':
            shows = shows.filter(hall__name = request.POST.get("hall", ''))


        todayDate = date.today()
        tomorrowDate = todayDate + timedelta(days=1)
        nextDate = todayDate + timedelta(days=2)

        todayShows = shows.filter(showDate=todayDate)
        tomorrowShows = shows.filter(showDate=tomorrowDate)
        nextDayShows = shows.filter(showDate=nextDate)

        shows = {'today':todayShows, 'tomorrow':tomorrowShows, 'nextDay':nextDayShows, 'movie':movie, 'showFilter': showFilter}

        # print("hall - ", request.POST["hall"])
        # for show in todayShows:
        #     print("time type - ", type(show.startTime))
        #     break

        return render(request, 'shows.html', shows)
