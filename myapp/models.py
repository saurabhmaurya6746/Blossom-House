# myapp/models.py

from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.title
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} on {self.date}"

 

class ContactEnquiry(models.Model):
    parent_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)  # optional
    mobile = models.CharField(max_length=15, blank=True, null=True)
    student_name = models.CharField(max_length=200)
    class_applying = models.CharField(max_length=50)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.parent_name} ({self.student_name})"
