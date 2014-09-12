from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User, Group, Permission

from whats_fresh_api.models import *
from django.contrib.gis.db import models

import os
import time
import sys
import datetime
import json

class ProductViewTestCase(TestCase):
    fixtures = ['test_fixtures']
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
  "name": "Ezri Dax",
  "variety": "Freshwater Eel",
   "alt_name": "Jadzia",
  "description": "That's not actually an eel, it's a symbiote.",
  "origin": "Trill",
  "season": "Season 7",
  "available": true,
  "market_price": "$32.64 per season",
  "link": "http://www.amazon.com/Star-Trek-Deep-Space-Nine/dp/B00008KA57/",
  "image": "/media/cat.jpg",
  "story_id": 2,
  "created": "2014-08-08 23:27:05.568395+00:00",
  "updated": "2014-08-08 23:27:05.568395+00:00"
}"""

    def test_url_endpoint(self):
       url = reverse('product-details', kwargs={'id': '1'})
       self.assertEqual(url, '/products/1')

    def test_json_equals(self):
        response = self.client.get(reverse('product-details', kwargs={'id': '1'})).content

        self.maxDiff = None

        parsed_answer = json.loads(response)
        expected_answer = json.loads(self.expected_json)

        self.assertEqual(parsed_answer, expected_answer)
