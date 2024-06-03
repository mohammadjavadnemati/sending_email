from django.shortcuts import render,redirect
from sending_email import settings
from django.core.mail import send_mail
# Create your views here.


def sending_email(request):
    if request.method == "POST":
        to_email = request.POST.get('email')

        subject = 'we glad that you can read this'
        message = 'i wish it work and you can read it '
        from_email = settings.EMAIL_HOST_USER
        to_list = [to_email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        redirect('')

    return render(request,'sending_email/confirm_email.html')