
import unittest

class TestApp (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass


    @classmethod
    def tearDownClass(cls):
        pass

    # test 1
    def test_one(self):
        self.assertEqual(1,1)

    # test 2
    def test_two(self):
        self.assertGreater(3,2)
