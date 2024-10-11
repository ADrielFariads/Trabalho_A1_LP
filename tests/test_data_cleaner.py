import sys, os
import pandas as pd
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , 'src')))

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

        #Removing the index for the test
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

        #Removing the index for the test
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

        #Removing the index for the test
        example = data_cleaner.add_black_white_level(example).reset_index(drop = True)
        result = result.reset_index(drop = True)

        pd.testing.assert_frame_equal(example, result)
    
    def test_white_equal_level(self):

        example_data = {
            'black_rating': [1400,1600],
            'white_rating': [1200,1200]
        }
        example = pd.DataFrame(example_data)

        result_data =  {
            'black_rating': [1400,1600],
            'white_rating': [1200,1200],
            'level_black_player' : ['high' , 'high'],
            'level_white_player' : ['medium' , 'medium']
        }
        result = pd.DataFrame(result_data)

        #Removing the index for the test
        example = data_cleaner.add_black_white_level(example).reset_index(drop = True)
        result = result.reset_index(drop = True)

        pd.testing.assert_frame_equal(example, result)


class Test_add_game_level(unittest.TestCase):

    def test_normal_case(self):

        example_data = {
            'black_rating': [1200,1500,2000],
            'white_rating': [1250,1400,2050]
        }
        example = pd.DataFrame(example_data)

        result_data =  {
            'black_rating': [1200,1500,2000],
            'white_rating': [1250,1400,2050],
            'game_level' : ['low', 'medium' , 'high']
        }
        result = pd.DataFrame(result_data)

        #Removing the index for the test
        example = data_cleaner.add_game_level(example).reset_index(drop = True)
        result = result.reset_index(drop = True)

        pd.testing.assert_frame_equal(example, result)

    def test_equal_rating(self):
    

        example_data = {
            'black_rating': [1200,1200],
            'white_rating': [1200,1200]
        }
        example = pd.DataFrame(example_data)

        result_data =  {
            'black_rating': [1200,1200],
            'white_rating': [1200,1200],
            'game_level' : ['high' , 'high'],
        }
        result = pd.DataFrame(result_data)

        #Removing the index for the test
        example = data_cleaner.add_game_level(example).reset_index(drop = True)
        result = result.reset_index(drop = True)

        pd.testing.assert_frame_equal(example, result)


class Test_cut_short_games(unittest.TestCase):

    def test_normal_case(self):

        example_data = {
            'turns': [1,2,3,20,35,55]
        }
        example = pd.DataFrame(example_data)

        result_data =  {

            'turns': [3,20,35,55]  
        }
        result = pd.DataFrame(result_data)

        #Removing the index for the test
        example = data_cleaner.cut_short_games(example).reset_index(drop = True)
        result = result.reset_index(drop = True)

        pd.testing.assert_frame_equal(example, result)
    
    def test_only_short_games(self):

        example_data = {
            'turns': [1,1,2,2]
        }
        example = pd.DataFrame(example_data)

        result_data =  {
            'turns': []
        }
        result = pd.DataFrame(result_data)
        
        #Removing the index and changing the type for the test
        example = data_cleaner.cut_short_games(example).reset_index(drop = True)
        result = result.reset_index(drop = True).astype('int64')


        pd.testing.assert_frame_equal(example, result)

    def test_without_short_games(self):

        example_data = {
            'turns': [15,25,72,42,666]
        }
        example = pd.DataFrame(example_data)

        result_data =  {

            'turns': [15,25,72,42,666]  
        }
        result = pd.DataFrame(result_data)
        
        #Removing the index for the test
        example = data_cleaner.cut_short_games(example).reset_index(drop = True)
        result = result.reset_index(drop = True)

        pd.testing.assert_frame_equal(example, result)

class TestGame_Duration(unittest.TestCase):


    def test_normal_case(self):
        example_data = {
           'turns': [10,20,30]
        }

        example = pd.DataFrame(example_data)
        
        result_data = {
            'turns': [10,20,30],
            'game_duration_in_turns': ['low','medium','high']
        }

        result = pd.DataFrame(result_data)

        #Removing the index for the test
        example = data_cleaner.add_game_duration(example).reset_index(drop = True)
        result = result.reset_index(drop = True)

        pd.testing.assert_frame_equal(example, result)

    def test_equal_data(self):

        example_data = {
           'turns': [10,10,10]
        }

        example = pd.DataFrame(example_data)
        
        result_data = {
            'turns': [10,10,10],
            'game_duration_in_turns': ['high','high','high']
        }

        result = pd.DataFrame(result_data)

        #Removing the index for the test
        example = data_cleaner.add_game_duration(example).reset_index(drop = True)
        result = result.reset_index(drop = True)

        pd.testing.assert_frame_equal(example, result)

class test_cut_duplicates(unittest.TestCase):
    def test_normal_case(self):

        example_data = {
            'moves': [1,2,2,3,3,4,5],

            'other_serie':['a','b','b','c','c','d','e']
        }
        example = pd.DataFrame(example_data)

        result_data =  {

            'moves': [1,2,3,4,5],

            'other_serie':['a','b','c','d','e']

        }
        result = pd.DataFrame(result_data)

        #Removing the index for the test
        example = data_cleaner.cut_duplicates(example).reset_index(drop = True)
        result = result.reset_index(drop = True)

        pd.testing.assert_frame_equal(example, result)
    
    def test_only_duplicate_games(self):

        example_data = {
            'moves': [1,1,1,1,1,1],

            'other_serie':['a','a','a','a','a','a']
        }
        example = pd.DataFrame(example_data)

        result_data =  {

            'moves': [1],

            'other_serie':['a'] 
        }
        result = pd.DataFrame(result_data)

        #Removing the index for the test
        example = data_cleaner.cut_duplicates(example).reset_index(drop = True)
        result = result.reset_index(drop = True)

        pd.testing.assert_frame_equal(example, result)

    def test_without_duplicate_games(self):

        example_data = {
            'moves': [1,2,3,4,5],
            'other_serie':['a','b','c','d','e']
        }
        example = pd.DataFrame(example_data)

        result_data =  {

            'moves': [1,2,3,4,5],
            'other_serie':['a','b','c','d','e']  
        }
        result = pd.DataFrame(result_data)

        #Removing the index for the test
        example = data_cleaner.cut_duplicates(example).reset_index(drop = True)
        result = result.reset_index(drop = True)

        pd.testing.assert_frame_equal(example, result)

if __name__ == "__main__":
    unittest.main()




