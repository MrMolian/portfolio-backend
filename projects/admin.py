from django.contrib import admin

# Register your models here.
from projects.models import Project,YearMessage

admin.site.register(Project)
admin.site.register(YearMessage)
