from django.contrib import admin
from .models import Tag, ProjectImage, Project, Experience, Education

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    inlines = [ProjectImageInline]
    search_fields = ("title", "description")
    list_filter = ("tags",)

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("job_title", "company_name", "start_date", "end_date")
    search_fields = ("job_title", "company_name", "description")
    list_filter = ("company_name", "start_date", "end_date")
    fieldsets = (
        (None, {
            'fields': ('job_title', 'company_name')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date')
        }),
        ('Description', {
            'fields': ('description',)
        }),
    )

class EducationAdmin(admin.ModelAdmin):
    list_display = ("certificate_title", "school_name", "start_date", "end_date")
    search_fields = ("certificate_title", "school_name", "description")
    list_filter = ("school_name", "start_date", "end_date")
    fieldsets = (
        (None, {
            'fields': ('certificate_title', 'school_name')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date')
        }),
        ('Description', {
            'fields': ('description',)
        }),
    )

admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(ProjectImage)  # Register ProjectImage independently

# Register your models here.
