from django.shortcuts import render, redirect
from MyMusic.account.views import get_profile
from MyMusic.album.models import AlbumModel


# Create your views here.
def home_page(request):
    profile = get_profile()
    if profile is None:
        return redirect('add-profile')

    context = {
        'album': AlbumModel.objects.all()
    }
    return render(request, 'common/home-with-profile.html', context=context)
