from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Movie
from shows.models import Show
from .filters import MovieFilter

# Create your views here.
@login_required(login_url='/login/')
def viewMovies(request):
    movies = Movie.objects.all()

    movieFilter = MovieFilter(request.GET, queryset=movies)
    movies = movieFilter.qs

    return render(request, 'viewMovie.html', {'movies':movies, 'movieFilter': movieFilter})

@login_required(login_url='/login/')
def viewMoviesByHall(request, hall):
    shows = Show.objects.filter(hall__name = hall)
    showList = []

    for show in shows:
        showList.append(show.movie.name)
    showList = set(showList)
    print(showList)

    movies = Movie.objects.all()
    movieList=[]
    for x in showList:
        movieList.append(movies.get(name=x))
    # print(movies)
    print(movieList)

    movieFilter = MovieFilter()
    # movieList = movieFilter.qs

    return render(request, 'viewMovie.html', {'movies':movieList,'hall':hall, 'movieFilter': movieFilter})

def movieInfo(request, id):
    movie = Movie.objects.get(id=id)
    link = movie.trailer.split('/')[-1]
    print("hall - ", request.POST["hall"])
    return render(request, 'movieInfo.html', {'movie':movie,'link':link, 'hall':request.POST["hall"]})
