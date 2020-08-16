from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Permission
from .models import (
    User,
    # LanguageModel,
    Contactinfo,
)

admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)

admin.site.register(User)
# admin.site.register(LanguageModel)
admin.site.register(Contactinfo)


admin.site.site_header = "Consult admin page"
admin.site.site_title = "Consult admin area"
admin.site.index_title = "Consult administration"
