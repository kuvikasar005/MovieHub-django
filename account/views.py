from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        if request.method == 'GET':
            return render(request, 'register.html')
        else:
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            username = request.POST['uname']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Already Taken')
                    return redirect('../register/')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Already Taken')
                    return redirect('../register/')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save()

                    subject = "MovieHub Account Created"

                    message = "Hello " + str(user.first_name).upper() + ",\n\nWelcome to MovieHub. We are happy to have you. We look forward to serve you with your best ever movie experience. \n\n Regards, \n MovieHub"
                    # print(message)

                    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


                    print('User Created')
                    return redirect('/login/')
            else:
                messages.info(request, 'Password Not Matching')
                return redirect('../register/')


def login(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        if request.method == 'GET':
            path = request.GET.get("next", "/home/")
            return render(request, 'login.html', {'path':path})
        else:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username = username, password = password)

            path = request.POST.get("next", "/home/")

            if user is not None:
                auth.login(request, user)
                print("path - ", path)
                return redirect(path)
            else:
                path = "/login/?next=" + path
                messages.info(request, 'Invalid Credentials')
                return redirect(path)

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def viewProfile(request):
    return render(request, 'customerProfile.html', {'user':request.user})

@login_required(login_url='/login/')
def editProfile(request):

    if request.method == 'GET':
        return render(request, 'editProfile.html', {'user':request.user})
    else:
        user = User.objects.get(username=request.user)

        # Get data from form
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]


        if user.email == email:
            # update to user object
            user.first_name = fname
            user.last_name = lname
            user.email = email

            # update to database and redirect
            user.save()
            messages.info(request, "Profile Updated")
            return redirect('/profile/')

        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Taken')
            return redirect('/profile/')
        else:
            # update to user object
            user.first_name = fname
            user.last_name = lname
            user.email = email

            # update to database and redirect
            user.save()
            messages.info(request, "Profile Updated")
            return redirect('/profile/')
