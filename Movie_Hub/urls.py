"""Movie_Hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from home.views import index,home
from account.views import register,login,logout,viewProfile,editProfile
from offer.views import viewOffer
from hall.views import viewHall
from movie.views import viewMovies,movieInfo,viewMoviesByHall
from shows.views import viewShows
from payment.views import orderSummary, payment
from ticket.views import bookTicket
from history.views import bookHistory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('home/', home),
    path('register/', register),
    path('login/', login, name="login"),
    path('logout/', logout),
    path('offer/', viewOffer),
    path('hall/', viewHall),
    path('profile/', viewProfile),
    path('profile/edit', editProfile, name="editProfile"),
    path('movie/', viewMovies, name='viewMovies'),
    path('movie/<int:id>/', movieInfo, name="movieInfo"),
    path('movie/<str:hall>/', viewMoviesByHall, name="viewMoviesByHall"),
    path('show/<str:movie>/', viewShows, name="viewShows"),
    path('orderSummary/', orderSummary, name="orderSummary"),
    path('payment/', payment, name="pay"),
    path('book/', bookTicket, name="book"),
    path('history/', bookHistory, name="orderHistory"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="resetPassword.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="resetPasswordSent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="resetPasswordForm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="resetPasswordSuccess.html"), name="password_reset_complete"),

]

#Submit email address form
#Email sent success messages
#Link to password reset in email
#Password successfully changer messages

#urlpattern for media root
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
