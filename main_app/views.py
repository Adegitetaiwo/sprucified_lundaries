from django.shortcuts import render
from booking_app.models import bookingSpace
from booking_app.forms import bookingForm
from contact.forms import contactForms
from django.core.mail import BadHeaderError, send_mail
from .models import customerTestimony, fourImageGallary, set_frequently_asked_question
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404

# Create your views here.

def index(request):
    booking_space = bookingSpace.objects.all()
    customer_testiony = customerTestimony.objects.all()
    four_image_gallary = fourImageGallary.objects.all()[:4]
    set_frequently_asked_questions = set_frequently_asked_question.objects.all()
    booking_form = bookingForm(request.POST or None)
    contact_form = contactForms(request.POST or None)

    if 'fullname' in request.POST:
        if booking_form.is_valid():
            send_mail('New Shedule Pickup | Sprucified Lundaries', 
                      f'Greetings, A new Pickup has been shedule by {booking_form.instance.fullname}. Please login to your admin dashboard to see full details',
                      'apostolictestimony@gmail.com', ['apostolictestimony@gmail.com'], fail_silently=True, html_message=f'<a href="{request.path_info}/admin">Admin Dasboard</a>')
            booking_form.save()
            messages.success(request, 'Valid form')

            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, 'Not a valid form')
            return HttpResponseRedirect(request.path_info)
    #contact form
    elif 'subject' in request.POST:
        if contact_form.is_valid():
            send_mail(f'Contact from {contact_form.instance.email} | Sprucified Lundaries',
                      f'Greetings, A new Pickup has been shedule by {contact_form.instance.first_name}. Please login to your admin dashboard to see full details',
                      'apostolictestimony@gmail.com', ['apostolictestimony@gmail.com'], fail_silently=True, html_message=f'<a href="{request.path_info}/admin">Admin Dasboard</a>')
            contact_form.save()
            messages.success(request, 'Valid form')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, 'Not a valid form')
            return HttpResponseRedirect(request.path_info)
    #even if all condition are not met
    else:

        content ={
            'four_image_gallary': four_image_gallary,
            'booking': booking_form,
            'contact': contact_form,
            'customer_testimony': customer_testiony,
            'set_frequently_asked_questions':set_frequently_asked_questions,
        }

        return render(request, 'index.html', content)
