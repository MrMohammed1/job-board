from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .models import Info

def send_message(request):
    myinfo = Info.objects.first()
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        
        # Send email
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],  # Replace with your email address
        )
        

    
    return render(request, 'contact.html', {'myinfo': myinfo})


