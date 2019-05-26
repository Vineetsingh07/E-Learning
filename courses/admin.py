from django.contrib import admin
from .models import Subject, Course, Module
# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug':('title',)}
	search_fields = ['title']

class ModuleInline(admin.StackedInline):
	model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['title', 'owner','subject', 'created', 'updated']
	list_filter = ['created', 'updated', 'subject']
	search_fields = ['title', 'subject']
	prepopulated_fields = {'slug':('title',)}
	raw_id_fields = ('owner', 'subject')
	inlines = [ModuleInline]

