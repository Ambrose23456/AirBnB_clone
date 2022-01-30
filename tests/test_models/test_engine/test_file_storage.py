#!/usr/bin/python3
'''
test file_storage module using unittest
'''

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Test cases"""

    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()
        return super().setUp()

    def tearDown(self):
        del(self.storage)
        del(self.model)
        return super().tearDown()

    def test_is_instance(self):
        """isInstance"""
        self.assertIsInstance(self.storage, FileStorage)

<<<<<<< HEAD
    def test_all(self):
        """
        test all method
        """
        pass
=======
>>>>>>> bade16480f75d625003ed55484a841e64f30f25e

if __name__ == '__main__':
    unittest.main()
