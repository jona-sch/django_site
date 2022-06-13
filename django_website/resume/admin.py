from django.contrib import admin

from resume.models import Experience


class ExperienceAdmin(admin.ModelAdmin):

    pass



admin.site.register(Experience, ExperienceAdmin)
