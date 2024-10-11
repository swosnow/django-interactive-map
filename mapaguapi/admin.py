from django.contrib import admin
from .models import Problem

class ProblemAdmin(admin.ModelAdmin):
    ...

admin.site.register(Problem, ProblemAdmin)
