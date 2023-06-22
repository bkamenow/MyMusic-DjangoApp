from django.contrib import admin

from MyMusic.album.models import AlbumModel


# Register your models here.


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'artist', 'genre', 'image', 'price')


admin.site.register(AlbumModel, AlbumAdmin)
