from django.shortcuts import render
from .models import Notice , Event 
from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactEnquiry
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    notices = Notice.objects.order_by('-created_at')[:5]  # latest 5 notices
    events = Event.objects.filter(date__gte=date.today()).order_by('date')[:5]
    return render(request, 'index.html', {
    'notices': notices,
    'events': events
})


def about(request):
    return render(request, 'about.html')

def event(request):
    return render(request, 'event.html')

# def gallery(request):
#     return render(request, 'gallery.html')

def faculty(request):
    return render(request, 'faculty.html')


 
def contact(request):
    if request.method == "POST":
        parent_name = request.POST.get('parent_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        student_name = request.POST.get('student_name')
        class_applying = request.POST.get('class_applying')
        message = request.POST.get('message')

        # Save to DB
        ContactEnquiry.objects.create(
            parent_name=parent_name,
            email=email,
            mobile=mobile,
            student_name=student_name,
            class_applying=class_applying,
            message=message
        )

        # Send email to school
        send_mail(
            "New Admission Enquiry Received",
            f"Parent/Guardian Name: {parent_name}\n"
            f"Email: {email}\n"
            f"Mobile: {mobile}\n"
            f"Student Name: {student_name}\n"
            f"Class Applying For: {class_applying}\n"
            f"Message: {message}",
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        messages.success(request, "Your enquiry has been submitted successfully!")
        return redirect('contact')

    return render(request, 'contact.html')
