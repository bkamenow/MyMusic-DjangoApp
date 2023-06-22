from MyMusic.account.models import UserModel
from MyMusic.album.models import AlbumModel


def get_album(pk):
    album = AlbumModel.objects.filter(pk=pk).get()
    return album


def get_albums():
    return AlbumModel.objects.all()


def get_profile():
    try:
        return UserModel.objects.get()
    except UserModel.DoesNotExist as ex:
        return None
