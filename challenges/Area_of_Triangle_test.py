import Area_of_Triangle_Very_Easy
import unittest

class area_of_Triangle_Test(unittest.TestCase):
    def test_area(self):
        self.assertEqual(Area_of_Triangle_Very_Easy.tri_area(3,10), 15)

    # This test is designed to fail for demonstration purposes.
    def test_decrement(self):
        self.assertEqual(Area_of_Triangle_Very_Easy.tri_area(5,4), 10)


unittest.main()