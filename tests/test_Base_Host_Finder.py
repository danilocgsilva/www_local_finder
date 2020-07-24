import unittest
import sys
sys.path.insert(1, "..")
from wwwlocalfinder.Base_Host_Finder import Base_Host_Finder

class test_Base_Host_Finder(unittest.TestCase):

    def setUp(self):
        self.wwwfinder = Base_Host_Finder()


    def test_can_get_linux_www_path(self):
        os_name = 'posix'
        self.wwwfinder.set_os_name(os_name)

        expected_result = "/var/www/html"
        returned_result = self.wwwfinder.get_www_path()

        self.assertEqual(expected_result, returned_result)


    def test_raise_exception_forget_to_set_os_name(self):
        with self.assertRaises(Exception):
            self.wwwfinder.get_www_path()


    def test_raise_exception_setting_non_existing_os(self):
        os_name = 'non_existent'
        self.wwwfinder.set_os_name(os_name)
        with self.assertRaises(Exception):
            self.wwwfinder.get_www_path()
