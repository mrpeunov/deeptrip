import unittest
import tours.services.get_tours as gt
import tours.services.get_h2 as gh2


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


class H2Test(unittest.TestCase):
    def test_month_str(self):
        self.assertEqual(gh2.get_month_str(0), "январе")
        self.assertEqual(gh2.get_month_str(11), "декабре")
