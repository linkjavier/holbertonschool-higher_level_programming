#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    

    def test_instance(self):
        obj = Base()
        self.assertIsInstance(obj, Base)

    def test_nb_objects_exists(self):
        obj = Base()
        failure_msg = 'global var __nb_objects not found'
        self.assertTrue(hasattr(obj, '_Base__nb_objects'), msg=failure_msg)

    def test_default_id(self):
        self.assertEqual(Base._Base__nb_objects, 0)
        objs = [Base() for x in range(5)]
        ans = [x.id for x in objs]
        target = [1, 2, 3, 4, 5]
        failure_msg = '{} and {} are different'.format(ans, target)
        self.assertListEqual(ans, target, msg=failure_msg)

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_manual_id(self):
        ids = [234, 456, 3445, 9999, 666, 45, 56]
        objs = [Base(x) for x in ids]
        self.assertListEqual([x.id for x in objs], ids)

    def test_attr_id_exists(self):
        obj = Base()
        failure_msg = 'property id not found'
        self.assertTrue(hasattr(obj, 'id'), msg=failure_msg)

    def test_mixed_ids(self):
        ids = [None, 111, None, 222, None, 333]
        objs = [Base(x) for x in ids]
        ans = [k.id for k in objs]
        target = [1, 111, 2, 222, 3, 333]
        failure_msg = '{} and {} are different'.format(ans, target)
        self.assertListEqual(ans, target, msg=failure_msg)

def test_pep8(self):
        """PEP8 Test"""
        style = pep8.StyleGuide(quiet=True)
        rectangle = "models/rectangle.py"
        test_rectangle = "tests/test_models/test_rectangle.py"
        result = style.check_files([rectangle, test_rectangle])
        self.assertEqual(result.total_errors, 1)
