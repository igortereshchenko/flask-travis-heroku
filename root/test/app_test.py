from root.app import app

import unittest

class TestApp (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass


    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_status(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code,200)


    def test_hello(self):
        result = self.app.get('/Bob')
        self.assertEqual(result.data, b'Hello, Bob')

