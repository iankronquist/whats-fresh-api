from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404

from whats_fresh_api.groups import *

class RolesTestCase(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user('admin_user',
                'admin_user@example.com', 'admin_user')
        self.admin_user.save()
        admin_user.groups.add(Administration)

        self.anon_user = User.objects.create_user('anon_user',
                'anon_user@example.com', 'anon_user')
        self.anon_user.save()
        anon_user.groups.add(Anonymous)

        self.data_entry_user = User.objects.create_user('data_entry_user',
                'data_entry_user@example.com', 'data_entry_user')
        self.data_entry_user.save()
        data_entry_user.groups.add(Data_entry)

    def test_user_permissions(self):
        self.assertEqual(admin_user.groups.filter(name='Administration'), True)
        self.assertEqual(anon_user.groups.filter(name='Anonymous'), True)
        self.assertEqual(data_entry_user.groups.filter(name='Data_entry'), True)
