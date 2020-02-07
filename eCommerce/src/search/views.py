from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView, DetailView


class SearchProductListView(ListView):
    template_name = "products/list.html"

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
            return Product.objects.filter(title__icontains=query)
        # none() can be changed to featured()
        return Product.objects.none()
