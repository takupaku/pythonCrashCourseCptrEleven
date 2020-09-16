import unittest
from city_function import city
class NameTestCase(unittest.TestCase):

    def test_citycountry(self):
        '''do value such as "santigo, chile" works?'''
        formatted_name=city('santigo', 'chile')
        self.assertEqual(formatted_name,'Santigo Chile')

unittest.main()
