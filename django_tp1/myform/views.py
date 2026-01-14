from django.shortcuts import render
from django . shortcuts import render
from . myforms import ContactForm

def contact ( request ):
    contact_form = ContactForm ()
    return render (request, 'myform/contact.html', { 'contact_form':contact_form})