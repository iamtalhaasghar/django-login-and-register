from users.admin import *
from users.models import OtpCode
from django.contrib import admin


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OtpCode)
