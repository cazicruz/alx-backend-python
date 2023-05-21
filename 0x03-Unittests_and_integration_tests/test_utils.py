#!/usr/bin/env python3
"""test case testing with paramerised.expand"""
from parameterized import parameterized
import unittest
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """ testing the access_nested_map method"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b":2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping,
                                    path: Sequence, expected: Any) -> None:
        """test the access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, b), expected)

    @parameterized.expand([
        ({},("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                            path:Sequence) -> None:
    """ test method to test the error expected from access_nested_map"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
