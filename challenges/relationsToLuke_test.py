import relationsToLuke_Easy
import unittest

class LukeTest(unittest.TestCase):

    def test_leah_sister(self):
        stringy = "Luke, I am your Sister"
        self.assertEquals(relationsToLuke_Easy.relations_Luke("Leah"), stringy)

if __name__ == "__main__":
    unittest.main()