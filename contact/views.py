from django.shortcuts import render, redirect
from home.models import Topbar, header_carousel_pics, Footer
from django.contrib import messages, auth

# Create your views here.
from .forms import ContactForm

def contact(request):
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    template = "contact/contact.html"
    if request.method == "POST":
        form =ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent')
            return redirect('contact')
      
    else:
        form = ContactForm()
    
    context ={
        'topbars': topbars,
        'footers': footers,
        'form': form,
    }
    return render(request, template, context)