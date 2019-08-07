from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Fundi, Category


def fundis(request):
    context = {
        'fundis': Fundi.objects.all(),
       
    }
    return render(request, 'fundi/fundis.html', context)



def fundi(request, fundi_id):
    fundi = get_object_or_404(Fundi, pk=fundi_id)
    context = {
        'fundi': fundi
    }
    return render(request, 'fundi/fundi.html', context)