#!/usr/bin/env python3
"""test case testing with paramerised.expand"""
from parameterized import parameterized
import unittest
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b":2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
        def test_access_nested_map(self, a: Mapping,
                                    b: Sequence, expected: Any) -> None:
        """test the access_nested_map method"""
        nested_map = a
        assert_equal(access_nested_map(nested_map, b), expected)
