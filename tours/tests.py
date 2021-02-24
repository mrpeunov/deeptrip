import unittest
import tours.services.get_tours as gt


class CalcTest(unittest.TestCase):
    def test_get_start_number(self):
        self.assertEqual(gt.get_start_number(0), 0)
        self.assertEqual(gt.get_start_number(1), 18)
        self.assertEqual(gt.get_start_number(2), 36)
        self.assertEqual(gt.get_start_number(3), 54)
        self.assertEqual(gt.get_start_number(4), 71)

    def test_get_count(self):
        self.assertEqual(gt.get_count(0), 17)
        self.assertEqual(gt.get_count(1), 18)
        self.assertEqual(gt.get_count(3), 17)
