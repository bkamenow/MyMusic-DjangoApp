from django.contrib import admin

from MyMusic.account.models import UserModel


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'age')


admin.site.register(UserModel, UserAdmin)
