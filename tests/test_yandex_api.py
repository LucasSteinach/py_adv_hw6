import unittest
import requests
from main import dir_create_YaDisk, TOKEN

class YaApiTester(unittest.TestCase):
    def test_dir_create_YaDisk_1 (self):
        self.assertIn('href', dir_create_YaDisk().json().keys())
        pass

    def test_dir_create_YaDisk_2(self):
        self.assertEqual(dir_create_YaDisk().status_code, 201)

    def test_dir_create_YaDisk_failed_1(self):
        self.assertTrue('href' not in dir_create_YaDisk().json().keys())

    def test_dir_create_YaDisk_failed_2(self):
        self.assertTrue(dir_create_YaDisk().status_code != 201)



