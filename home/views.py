from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from movie.models import Movie

# Create your views here.

def index(request):
    #return render(request, 'hello.html', {'name': 'Vikas'})
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        movies = Movie.objects.all()
        return render(request, 'index.html', {'movies':movies})

@login_required(login_url='/login/')
def home(request):

    return render(request, 'customerHome.html')
