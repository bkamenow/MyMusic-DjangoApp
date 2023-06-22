from django.shortcuts import render, redirect

from helpers.helper import get_album
from MyMusic.album.forms import CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from MyMusic.account.views import get_profile


# Create your views here.


def add_album(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateAlbumForm()
    else:
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'album/add-album.html', context=context)


def album_details(request, pk):
    album = get_album(pk)
    profile = get_profile()

    context = {
        'album': album,
        'profile': profile
    }
    return render(request, 'album/album-details.html', context=context)


def edit_album(request, pk):
    profile = get_profile()
    album = get_album(pk)

    if request.method == 'GET':
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'profile': profile,
        'form': form,
        'album': album,
    }

    return render(request, 'album/edit-album.html', context=context)


def delete_album(request, pk):
    profile = get_profile()
    album = get_album(pk)

    if request.method == 'GET':
        form = DeleteAlbumForm(instance=album)
    else:
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'profile': profile,
        'album': album,
        'form': form,
    }

    return render(request, 'album/delete-album.html', context=context)
