from django.shortcuts import render, redirect

from helpers.helper import get_profile, get_albums
from MyMusic.account.forms import CreateProfileForm


def add_profile(request):
    if get_profile() is not None:
        return redirect('home-page')

    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    context = {
        'form': form
    }

    return render(request, 'common/home-no-profile.html', context=context)


def profile_details(request):
    profile = get_profile()
    albums = get_albums()

    context = {
        'profile': profile,
        'albums_length': len(albums),
    }

    return render(request, 'account/profile-details.html', context=context)


def delete_profile(request):
    profile = get_profile()
    albums = get_albums()

    if request.method == 'GET':
        profile.delete()
        albums.delete()
        return redirect('home-page')

    context = {
        'profile': profile
    }

    return render(request, 'account/profile-delete.html', context=context)
