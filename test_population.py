import unittest
from population import city_info
class NameTestCase(unittest.TestCase):

    def test_citycountry(self):
        '''do value such as "santigo, chile" works?'''
        formatted_name=city_info('santigo', 'chile', '10000')
        self.assertEqual(formatted_name,'Santigo Chile 10000')

unittest.main()
