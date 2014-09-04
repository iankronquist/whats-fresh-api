from django.http import (HttpResponse,
                         HttpResponseNotFound,
                         HttpResponseServerError)
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.utils.datastructures import MultiValueDictKeyError

from whats_fresh_api.models import *
from whats_fresh_api.forms import *
from whats_fresh_api.functions import *

import json


def preparation(request, id=None):
    if request.method == 'POST':
        post_data = request.POST.copy()
        errors = []

        preparation_form = PreparationForm(post_data)
        if preparation_form.is_valid() and not errors:
            preparation = Preparation.objects.create(**preparation_form.cleaned_data)
            preparation.save()
            return HttpResponseRedirect(reverse('preparations-list-edit'))
        else:
            pass
    else:
        preparation_form = PreparationForm()

    title = "New Preparation"
    post_url = reverse('new-preparation')

    message = "Fields marked with bold are required."

    return render(request, 'preparation.html', {
        'parent_url': reverse('preparations-list-edit'),
        'parent_text': 'Preparation List',
        'message': message,
        'title': title,
        'post_url': post_url,
        'errors': [],
        'preparation_form': preparation_form,
    })


def preparation_list(request):
    return HttpResponse('Preparation List')
