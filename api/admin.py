from django.contrib import admin
from api.models import CSUClass, CSUClassDays, CSUTags
# Register your models here.

admin.site.register(CSUTags)
admin.site.register(CSUClass)
admin.site.register(CSUClassDays)