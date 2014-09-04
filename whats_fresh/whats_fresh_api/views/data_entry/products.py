from django.http import (HttpResponse,
                         HttpResponseNotFound,
                         HttpResponseServerError)
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.utils.datastructures import MultiValueDictKeyError

from whats_fresh_api.models import *
from whats_fresh_api.forms import *

import json


def product_list(request):
    products = Product.objects.all()
    products_list = []

    for product in products:
        product_data = {}
        product_data['name'] = product.name
        product_data['modified'] = product.modified.strftime("%I:%M %P, %d %b %Y")
        product_data['description'] = product.description
        product_data['link'] = reverse('edit-product', kwargs={'id': product.id})

        product_data['preparations'] = [
            preparation.name for preparation in product.preparations.all()]

        if len(product_data['description']) > 100:
            product_data['description'] = product_data['description'][:100] + "..."

        products_list.append(product_data)

    return render(request, 'products_list.html', {
        'new_url': reverse('new-product'),
        'new_text': "New product",
        'title': "All products",
        'item_classification': "product",
        'item_list': products_list,
    })


def product(request, id=None):
    pass
