import unittest
import sys
sys.path.insert(1, "..")
from wwwlocalfinder.functions import get_www

class test_functions(unittest.TestCase):

    def test_can_get_default_www_path(self):
        expected_result = "/var/www/html"
        os_name = 'posix'
        self.assertEqual(expected_result, get_www(os_name))
