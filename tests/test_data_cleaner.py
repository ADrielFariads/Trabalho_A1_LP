import sys, os
import pandas as pd
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import data_cleaner

class TestQuantil(unittest.TestCase):

    def test_median(self):
        self.assertEqual(data_cleaner.quantile([1,2,3],2), {1: 2.0})

    def test_quantiles(self):
        result = data_cleaner.quantile([1,2,3,4,5,6,7], 3)
        self.assertEqual(result, {1: 3.0, 2: 5.0})

    def test_one_division(self):
        self.assertEqual(data_cleaner.quantile([1,2,3], 1), {})

    def test_zero_divisions(self):
        self.assertEqual(data_cleaner.quantile([1,2,3], 0), {})
