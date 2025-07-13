from django.contrib import admin

# Register your models here.
 
from .models import Notice, Event , ContactEnquiry

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'text')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at')
    search_fields = ('title',)
    list_filter = ('date',)
 
@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'email', 'student_name', 'class_applying', 'submitted_at')
    search_fields = ('parent_name', 'email', 'student_name')
