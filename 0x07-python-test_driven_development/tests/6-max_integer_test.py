#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Checks various test cases of a given list """

    def test_Max_Beginning(self):
        """Tests a list with max value at beginning"""
        sample = [5, 2, 4, 2, 1]
        self.assertEqual(max_integer(sample), 5)

    def test_Max_End(self):
        """Tests a list with max value at the end"""
        sample = [1, 2, 4, 2, 5]
        self.assertEqual(max_integer(sample), 5)

    def test_Max_Middle(self):
        """Tests a list with max value at the middle"""
        sample = [1, 2, 4, 2, 1]
        self.assertEqual(max_integer(sample), 4)

    def test_Max_with_Negative(self):
        """Tests a list with a negative number"""
        sample = [5, 2, 4, 2, -1]
        self.assertEqual(max_integer(sample), 5)

    def test_Max_Negatives_only(self):
        """Tests a list with only negative numbers"""
        sample = [-5, -2, -4, -2, -1]
        self.assertEqual(max_integer(sample), -1)

    def test_Max_Single_Value(self):
        """Tests a list with single value"""
        sample = [5]
        self.assertEqual(max_integer(sample), 5)

    def test_Max_Empty(self):
        """Tests an empty list"""
        sample = []
        self.assertEqual(max_integer(sample), None)
