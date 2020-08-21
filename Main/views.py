from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse_lazy
from Main.forms import SubscriberForm,ContactForm
from django.views.generic import ListView,CreateView,TemplateView
from Main.models import City,ContactInfo,AboutProject
# Create your views here.

class MainClassView(ListView):
    model = City
    template_name = 'main.html'


class SubscriberCreateView(CreateView):
    form_class = SubscriberForm
    template_name = None
    http_method_names = ('post',)
    success_url = reverse_lazy('main:home')

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


class ContactSubjectView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    # http_method_names = ('post',)
    success_url = reverse_lazy('main:home')

class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contactInfo = ContactInfo.objects.get()
        context['contactInfo'] = contactInfo
        context['form'] = ContactForm()
        return context

class AboutUsView(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aboutUs = AboutProject.objects.get()
        context['aboutUs'] = aboutUs
        return context

class PrivacyPolicyView(TemplateView):
    template_name = 'policies.html'

class TermsOfUseView(TemplateView):
    template_name = 'terms.html'

