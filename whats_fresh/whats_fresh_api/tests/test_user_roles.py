from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import Group, Permission, User
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from whats_fresh_api.groups import *

class RolesTestCase(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user('admin_user',
                'admin_user@example.com', 'admin_user')
        self.admin_user.save()
        self.anon_user = User.objects.create_user('anon_user',
                'anon_user@example.com', 'anon_user')
        self.anon_user.save()
        self.data_entry_user = User.objects.create_user('data_entry_user',
                'data_entry_user@example.com', 'data_entry_user')
        self.data_entry_user.save()

        admin_group = Group(name='Administration Users')
        admin_group.save()
        anon_group = Group(name='Anonymous Users')
        anon_group.save()
        data_entry_group = Group(name='Data Entry Users')
        data_entry_group.save()

        self.admin_user.groups.add(admin_group)
        self.anon_user.groups.add(anon_group)
        self.data_entry_user.groups.add(data_entry_group)

    def test_user_permissions(self):
        self.assertEqual(self.admin_user.groups.filter(name='Administration Users').exists(), True)
        self.assertEqual(self.anon_user.groups.filter(name='Anonymous Users').exists(), True)
        self.assertEqual(self.data_entry_user.groups.filter(name='Data Entry Users').exists(), True)
