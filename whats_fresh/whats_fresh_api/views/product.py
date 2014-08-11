from django.http import (HttpResponse,
                         HttpResponseNotFound,
                         HttpResponseServerError)
from whats_fresh_api.models import Vendor, Product, VendorProduct
from django.forms.models import model_to_dict
import json


def product_list(request):
    data = {}
    product_list = Product.objects.all()

    if len(product_list) == 0:
        data['error'] = {
            'error_status': True,
            'error_level': 'Important',
            'error_text': 'Could not find any products!',
            'error_name': 'No products'
        }
        return HttpResponseNotFound(
            json.dumps(data),
            content_type="application/json"
        )

    try:
        for product in product_list:
            data[str(product.id)] = model_to_dict(
                product, fields=[], exclude=[])
            del data[str(product.id)]['id']
            del data[str(product.id)]['preparations']
            del data[str(product.id)]['image_id']

            data[str(product.id)]['image'] = product.image_id.image.url
            data[str(product.id)]['created'] = str(product.created)
            data[str(product.id)]['modified'] = str(product.modified)

        data['error'] = {
            'error_status': False,
            'error_level': None,
            'error_text': None,
            'error_name': None
        }
        return HttpResponse(json.dumps(data), content_type="application/json")

    except:
        data['error'] = {
            'error_status': True,
            'error_level': 'Severe',
            'error_text': 'An unknown error occurred processing the products',
            'error_name': 'Unknown'
        }
        return HttpResponseServerError(
            json.dumps(data),
            content_type="application/json"
        )


def product_details(request, id=None):
    data = {}

    try:
        product = Product.objects.get(id=id)
    except Exception as e:
        data['error'] = {
            'error_status': True,
            'error_level': 'Important',
            'error_text': 'Product with id %s not found!' % id,
            'error_name': 'Product Not Found'
        }
        return HttpResponse(
            json.dumps(data),
            content_type="application/json"
        )

    try:
        data = model_to_dict(product, fields=[], exclude=[])
        del data['id']
        del data['preparations']
        del data['image_id']

        data['image'] = product.image_id.image.url
        data['created'] = str(product.created)
        data['updated'] = str(product.modified)

        data['error'] = {
            'error_status': False,
            'error_level': None,
            'error_text': None,
            'error_name': None
        }
        return HttpResponse(json.dumps(data), content_type="application/json")

    except:
        error_text = 'An unknown error occurred processing product %s' % id
        data['error'] = {
            'error_status': True,
            'error_level': 'Severe',
            'error_text': error_text,
            'error_name': 'Unknown'
        }
        return HttpResponseServerError(
            json.dumps(data),
            content_type="application/json"
        )