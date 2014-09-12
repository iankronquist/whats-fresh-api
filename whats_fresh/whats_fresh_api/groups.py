from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from whats_fresh_api.models import *

if (Group.objects.filter(name='Administration').exists()):
    pass
else:
    administration = Group(name='Administration')
    administration.save()
    admin_model = ContentType.objects.get(app_label='whats_fresh_api',
            model='Vendor')

if not Group.objects.filter(name='Anonymous'):
    anonymous = Group(name='Anonymous')
    anonymous.save()

if not Group.objects.filter(name='Data Entry'):
    data_entry = Group(name='Data Entry')
    data_entry.save()
