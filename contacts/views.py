from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        email = request.POST['email']
        phone = request.POST['phone']
        name = request.POST['name']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']

        # Check if user has made an inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listig')
                return redirect('/listing/'+listing_id)

        contact = Contact(listing_id=listing_id, listing=listing, email=email, phone=phone, name=name, message=message, user_id=user_id)

        contact.save()

        # Send email
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
            'acozeljkovic1989@gmail.com',
            [realtor_email, 'acozeljkovic@gmail.com'],
            fail_silently=True
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')

        return redirect('/listings/'+listing_id)

