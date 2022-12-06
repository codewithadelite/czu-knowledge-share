from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(StaffCategory)
admin.site.register(Administrator)
admin.site.register(Student)
admin.site.register(File)
admin.site.register(FilePermission)
admin.site.register(Subject)
admin.site.register(Comment)
admin.site.register(Task)
