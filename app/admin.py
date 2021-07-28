from django.contrib import admin

# Register your models here.

from .models import Task01, Task02, Task03

admin.site.register(Task01)
admin.site.register(Task02)
admin.site.register(Task03)