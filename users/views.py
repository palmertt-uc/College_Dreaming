from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from universities.models import Institutions
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })


@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('login')
    return render(request, 'users/delete.html')


@login_required
def favourite_add(request, pk):
    university = get_object_or_404(Institutions, pk=pk)
    if university.favorite.filter(id=request.user.id).exists():
        university.favorite.remove(request.user)
    else:
        university.favorite.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def profile(request):
    saved = Institutions.objects.filter(favorite=request.user)

    if request.method == 'POST':
        user_update = UserUpdateForm(request.POST, instance=request.user)
        profile_update = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if user_update.is_valid() and profile_update.is_valid():
            user_update.save()
            profile_update.save()
            messages.success(request, 'Account Updated')
            return redirect('profile')
    else:
        user_update = UserUpdateForm(instance=request.user)
        profile_update = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_update': user_update,
        'profile_update': profile_update,
        'saved': saved
    }

    return render(request, 'users/profile.html', {'saved': saved, 'user_update': user_update,
                                                  'profile_update': profile_update})
