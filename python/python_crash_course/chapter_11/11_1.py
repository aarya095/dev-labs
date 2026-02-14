from city_functions import display_city_info
import unittest 

class TestCityFunctions(unittest.TestCase):
    
    def test_display_city_info(self):

        formatted_city_info = display_city_info('Mumbai','India')
        self.assertEqual(formatted_city_info, 'Mumbai, India')

if __name__ == '__main__':
    unittest.main()