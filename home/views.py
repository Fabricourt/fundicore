from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.contrib.admin.views.decorators import staff_member_required
from home.models import Topbar,header_carousel_pics, Footer
from services.models import Service
from abouts.models import About
from blog.models  import Post
from fundi.models  import Fundi
from django.views.generic import (
    ListView,
)

def index(request):
    abouts = About.objects.order_by('-reload').filter(is_published=True)[:1]
    services = Service.objects.order_by('reload').filter(is_published=True)[:4]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    header_carousel_picss = header_carousel_pics.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    
    posts = Post.objects.all()[:3]
    fundis = Fundi.objects.all()[:4]

    context = {
        'fundis': fundis,
        'abouts': abouts,
        'services': services,
        'posts': posts,
        'topbars': topbars,
        'header_carousel_picss': header_carousel_picss,
        'footers': footers,
    }
    return render(request, 'home/home.html', context) 


def about(request):
    abouts = About.objects.order_by('-reload').filter(is_published=True)[:1]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]

    context = {
        'abouts': abouts,
        'topbars': topbars,
        'footers': footers,
    }
    return render(request, 'home/about.html') 




@staff_member_required
def mobile(request):
    return render(request, 'home/mobile.html') 

@staff_member_required
def tablet(request):
    return render(request, 'home/tablet.html') 

@staff_member_required
def laptop(request):
    return render(request, 'home/laptop.html') 