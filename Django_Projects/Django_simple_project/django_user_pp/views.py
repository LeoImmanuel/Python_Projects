from django.shortcuts import render, redirect

# Import for Sign-Up/Registration setup
from django_user_pp.forms import UserInfoForm, UserProfileInfoForm

# Imports for Login setup
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# View for Sign-Up/Registration setup
def reg_index(request):
    registered = False

    if request.method == 'POST':
        user_reg_form = UserInfoForm(data=request.POST)
        profile_reg_form = UserProfileInfoForm(data=request.POST)

        if user_reg_form.is_valid() and profile_reg_form.is_valid():
            user = user_reg_form.save()
            user.set_password(user.password)  # Hashes the password
            user.save()

            profile = profile_reg_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

            # Automatically log the user in and redirect to the homepage
            login(request, user)
            return redirect('home')  # Redirects to the homepage after signup
        else:
            print(user_reg_form.errors, profile_reg_form.errors)
    else:
        # Ensure these are instances, not classes
        user_reg_form = UserInfoForm()
        profile_reg_form = UserProfileInfoForm()

    return render(request, 'django_user_pp/user_signup.html', {
        'user_reg_form': user_reg_form,
        'profile_reg_form': profile_reg_form,
        'registered': registered
    })


# View for Log-in/Log-out setup
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))  # Redirect to homepage
            else:
                return HttpResponse("Account not Active")
        else:
            print("Invalid login attempt")
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'django_user_pp/user_login.html')

@login_required    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))  # Redirect to homepage



    
