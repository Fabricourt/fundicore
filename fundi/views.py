from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Fundi, Category


def fundi(request):
    context = {
        'fundis': Fundi.objects.all(),
       
    }
    return render(request, 'fundi/fundi.html', context)


class FundiListView(ListView):
    model = Fundi
    template_name = 'fundi/fundi.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'fundis'
    ordering = ['-created_on']
    paginate_by = 6


class UserFundiListView(ListView):
    model = Fundi
    template_name = 'fundi/user_fundis.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'fundis'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Fundi.objects.filter(fundi_name=user).order_by('-created_on')


class FundiDetailView(DetailView):
    model = Fundi


class FundiCreateView(LoginRequiredMixin, CreateView):
    model = Fundi
    fields = ['title', 'Fundi_name','town','skill','service_charge','resume','address','phone1','phone2','email','facebook','twitter','linkedin','instagram','youtube','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6','is_published','created_on']
    
    def form_valid(self, form):
        form.instance.fundi_name = self.request.user
        return super().form_valid(form)


class FundiUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Fundi
    fields = ['title', 'Fundi_name','town','skill','service_charge','resume','address','phone1','phone2','email','facebook','twitter','linkedin','instagram','youtube','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6','is_published','created_on']

    def form_valid(self, form):
        form.instance.fundi_name = self.request.user
        return super().form_valid(form)

    def test_func(self):
        fundi = self.get_object()
        if self.request.user == fundi.fundi_name:
            return True
        return False


class FundiDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Fundi
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == fundi.author:
            return True
        return False

