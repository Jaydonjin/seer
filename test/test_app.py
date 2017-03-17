import json
import unittest

import app
from app import create_app


class HelloWorldTestCase(unittest.TestCase):
    def setUp(self):
        self.client = create_app('test').test_client()

    def test_version(self):
        response = self.client.get('/seer/api/v1/version', follow_redirects=True)
        self.assertDictEqual(dict(version=app.__version__), json.loads(response.data))

    def test_faq(self):
        response = self.client.get('/seer/faq.htm')
        self.assertEqual('<!--Newegg-->', response.data)
