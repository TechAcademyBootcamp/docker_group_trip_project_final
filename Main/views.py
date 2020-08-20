from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse_lazy
from Main.forms import SubscriberForm
from django.views.generic import ListView,CreateView
from Main.models import City
# Create your views here.

class MainClassView(ListView):
    model = City
    template_name = 'main.html'


class SubscriberCreateView(CreateView):
    form_class = SubscriberForm
    template_name = None
    http_method_names = ('post',)
    success_url = reverse_lazy('home')

    def get_success_url(self):
        redirect_url = self.request.GET.get('redirect_url',self.success_url)
        return redirect_url
#
    def form_valid(self, form):
        messages.success(self.request,'Subscribe oldunuz')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request,form.errors)
        redirect_url = self.request.GET.get('redirect_url',self.success_url)
        return redirect(redirect_url)

class CitySinglePage(ListView):
    model = City
    template_name = 'city_single_page.html'