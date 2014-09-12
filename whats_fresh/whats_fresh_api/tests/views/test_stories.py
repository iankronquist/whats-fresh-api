from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from whats_fresh_api.models import *
from django.contrib.gis.db import models
from django.contrib.auth.models import User, Group, Permission

import json


class StoriesTestCase(TestCase):
    fixtures = ['whats_fresh_api/tests/testdata/test_fixtures.json']

    def setUp(self):

        user = User.objects.create_user(username='test', password='pass')
        admin_group = Group(name='Administration Users')
        admin_group.save()
        user.groups.add(admin_group)
        self.client.post(reverse('login'), {'username':'test', 'password':'pass'})


        self.expected_json = """
{
    "error": {
        "error_status": false,
        "error_name": null,
        "error_text": null,
        "error_level": null
    },
    "story": "These are the voyages of the Starfish Enterblub; her five year mission -- to seek out new fish and new fishilizations..."
}"""

    def test_url_endpoint(self):
        url = reverse('story-details', kwargs={'id': '1'})
        self.assertEqual(url, '/stories/1')

    def test_json_equals(self):
        response = self.client.get(reverse('story-details', kwargs={'id': '1'})).content
        parsed_answer = json.loads(response)

        expected_answer = json.loads(self.expected_json)
        self.assertTrue(parsed_answer == expected_answer)
