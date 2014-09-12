from authority import permissions
from whats_fresh_api.models import *
from django.contrib.gis.db import models

import authority

"""
class EditingPermission(permissions.BasePermission):
    label = 'editing'

authority.register(Product, EditingPermission)
authority.register(Vendor, EditingPermission)
authority.register(Preparation, EditingPermission)
authority.register(Image, EditingPermission)
authority.register(Story, EditingPermission)
"""

vendor_model = ContentType.objects.get(app_label='whats_fresh_api', model='vendor')
product_model = ContentType.objects.get(app_label='whats_fresh_api',
        model='product')
preparation_model = ContentType.objects.get(app_label='whats_fresh_api',
        model='preparation')
image_model = ContentType.objects.get(app_label='whats_fresh_api', model='image')
story_model = ContentType.objects.get(app_label='whats_fresh_api', model='story')

editing = Permission(name='Editing', codename='editing',
        content_type=vendor_model)
