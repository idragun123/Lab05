from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView
from .models import Phones
# Create your views here.


class CatalogView(TemplateView):
    template_name = 'index.html'
    def get(self , request):
        all_catalog = Phones.objects.all()
        context = {
            'all': all_catalog,
        }
        return render(request, self.template_name, context)



