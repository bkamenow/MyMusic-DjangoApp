from django.urls import path

from MyMusic.account.views import profile_details, delete_profile, add_profile

urlpatterns = [

    path('add/', add_profile, name='add-profile'),
    path('details/', profile_details, name='profile-details'),
    path('delete/', delete_profile, name='delete-profile'),
]
