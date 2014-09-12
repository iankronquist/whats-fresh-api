from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from whats_fresh_api.models import *
from django.contrib.gis.db import models
from django.contrib.auth.models import User, Group, Permission

import json


class VendorsProductsTestCase(TestCase):
    fixtures = ['whats_fresh_api/tests/testdata/test_fixtures.json']

    def setUp(self):

        user = User.objects.create_user(username='test', password='pass')
        admin_group = Group(name='Administration Users')
        admin_group.save()
        user.groups.add(admin_group)
        self.client.post(reverse('login'), {'username':'test', 'password':'pass'})


        # In the test fixtures, there are two vendors. Only vendor
        # 1 sells Product 2. 
        self.expected_json = """
{
    "error": {
        "error_status": false,
        "error_name": null,
        "error_text": null,
        "error_level": null
    },
    "1": {
        "name": "No Optional Null Fields Are Null",
        "status": true,
        "description": "This is a vendor shop.",
        "lat": 37.833688,
        "long": -122.478002,
        "street": "1633 Sommerville Rd",
        "city": "Sausalito",
        "state": "CA",
        "zip": "94965",
        "location_description": "Location description",
        "contact_name": "A. Persson",
        "phone": 5417377627,
        "website": "http://example.com",
        "email": "a@perr.com",
        "story": 1,
        "ext": {},
        "created": "2014-08-08 23:27:05.568395+00:00",
        "updated": "2014-08-08 23:27:05.568395+00:00",
        "products": {
            "1": {
                "name": "Starfish Voyager",
                "preparation": "Live"
            },
            "2": {
                "name": "Ezri Dax",
                "preparation": "Live"
            }
        }
    }
}"""

    def test_url_endpoint(self):
       url = reverse('vendors-products', kwargs={'id': '2'})
       self.assertEqual(url, '/vendors/products/2')

    def test_json_equals(self):
        response = self.client.get(
            reverse('vendors-products', kwargs={'id': '2'})).content
        parsed_answer = json.loads(response)

        expected_answer = json.loads(self.expected_json)
        self.assertTrue(parsed_answer == expected_answer)
