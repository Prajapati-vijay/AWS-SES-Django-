from django.http import HttpResponse
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.shortcuts import render


def home(request):
    # ctx = {
    #     'user': "Vijay"
    # }
    message = get_template('index.html').render()
    msg = EmailMessage(
        'Test mail using SES',
        message,
        'kumar.vijay@gmail.com',#Sender Email
        ['vijay@gmail.com'],# Reciever email
    )
    msg.content_subtype ="html"# Main content is now text/html
    msg.send()
    print("Mail successfully sent")   
    
    return render(request,"index.html")    