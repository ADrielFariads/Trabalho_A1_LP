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

class Test_add_black_white_level(unittest.TestCase):

    def test_normal_case(self):

        example_data = {
            'black_rating': [1200,1500,2000],
            'white_rating': [1250,1400,2050]
        }
        example = pd.DataFrame(example_data)

        result_data =  {
            'black_rating': [1200,1500,2000],
            'white_rating': [1250,1400,2050],
            'level_black_player' : ['low', 'medium' , 'high'],
            'level_white_player' : ['low', 'medium' , 'high']
        }
        result = pd.DataFrame(result_data)

        example = data_cleaner.add_black_white_level(example).reset_index(drop = True)
        result = result.reset_index(drop = True)

        pd.testing.assert_frame_equal(example, result)

    def test_equal_level(self):

        example_data = {
            'black_rating': [1200,1200],
            'white_rating': [1200,1200]
        }
        example = pd.DataFrame(example_data)

        result_data =  {
            'black_rating': [1200,1200],
            'white_rating': [1200,1200],
            'level_black_player' : ['high' , 'high'],
            'level_white_player' : ['high' , 'high']
        }
        result = pd.DataFrame(result_data)

        example = data_cleaner.add_black_white_level(example).reset_index(drop = True)
        result = result.reset_index(drop = True)

        pd.testing.assert_frame_equal(example, result)

    def test_black_equal_level(self):

        example_data = {
            'black_rating': [1200,1200],
            'white_rating': [1400,1600]
        }
        example = pd.DataFrame(example_data)

        result_data =  {
            'black_rating': [1200,1200],
            'white_rating': [1400,1600],
            'level_black_player' : ['medium' , 'medium'],
            'level_white_player' : ['high' , 'high']
        }
        result = pd.DataFrame(result_data)

        example = data_cleaner.add_black_white_level(example).reset_index(drop = True)
        result = result.reset_index(drop = True)

        pd.testing.assert_frame_equal(example, result)
    
    def test_white_equal_level(self):

        example_data = {
            'black_rating': [1200,1200],
            'white_rating': [1400,1600]
        }
        example = pd.DataFrame(example_data)

        result_data =  {
            'black_rating': [1200,1200],
            'white_rating': [1400,1200],
            'level_black_player' : ['high' , 'high'],
            'level_white_player' : ['medium' , 'medium']
        }
        result = pd.DataFrame(result_data)

        example = data_cleaner.add_black_white_level(example).reset_index(drop = True)
        result = result.reset_index(drop = True)

        pd.testing.assert_frame_equal(example, result)


