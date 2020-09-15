from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView , DetailView
from Tours.models import Tours
from django.core.paginator import Paginator

# Create your views here.

class ToursPage(ListView):
    model = Tours
    template_name = 'tourspage.html'
    paginate_by = 1
    def get_context_data(self,*args , **kwargs):
        page = self.request.GET.get('page', 1) if self.request.GET.get('page', 1) != '' else 1
        data = self.get_queryset()
        context = super().get_context_data(**kwargs)
        if data:
            paginator = Paginator(data, self.paginate_by)
            results = paginator.page(page)
            index = results.number - 1
            max_index = len(paginator.page_range)
            start_index = index - 5 if index >= 5 else 0
            end_index = index + 5 if index <= max_index - 5 else max_index
            context['page_range'] = list(paginator.page_range)[start_index:end_index]
        context["tours"] = Tours.objects.all
        return context
    


class ToursSinglePage(DetailView):
    template_name = 'tours_single_page.html'
    model = Tours


