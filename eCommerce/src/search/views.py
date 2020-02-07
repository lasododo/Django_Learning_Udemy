from django.shortcuts import render
from products.models import Product
from django.db.models import Q
from django.views.generic import ListView, DetailView


class SearchProductListView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductListView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    """
        __contains = field contains the parameter ( title__icontains = 'HAT' )
        __iexact = field is exactly the parameter ( title__iexact = 'HAT' )
    """
    def get_queryset(self, *args, **kwargs):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')  # request.GET.get('q', "Shirt")  -> will lookup shirt if None
        print(query)
        if query is not None:
            return Product.objects.search(query)
            # Product.objects.filter(lookups).distinct()
        # none() can be changed to featured()
        return Product.objects.none()
