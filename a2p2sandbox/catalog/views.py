from django.shortcuts import render
from django.views import generic

from .models import CatalogItem


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'catalog/index.html'
    context_object_name = 'catalog_items'

    def get_queryset(self):
        return CatalogItem.objects.order_by('created_timestamp')


class CatalogItemView(generic.DetailView):
    model = CatalogItem
    context_object_name = 'catalog_item'
    template_name = 'catalog/detail.html'

