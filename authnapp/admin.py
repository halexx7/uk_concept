from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UkUser


class UkUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "age"),
            },
        ),
    )


admin.site.register(UkUser, UkUserAdmin)