import unittest

from isr.cold_ops import check_layout, flight_time_min
from isr.spec_gap import max_range_m


class TestISR(unittest.TestCase):
    def test_range_ordering(self):
        self.assertGreater(max_range_m("person", "detect"), max_range_m("person", "identify"))
        self.assertGreater(max_range_m("vehicle", "detect"), max_range_m("person", "detect"))

    def test_cold_costs_time(self):
        self.assertLess(flight_time_min(25, -20), flight_time_min(25, 20))
        self.assertGreater(flight_time_min(25, -20, heated=True), flight_time_min(25, -20))

    def test_glove_layout(self):
        self.assertEqual(len(check_layout([("arm", 20, 20), ("tiny", 8, 8)])), 1)


if __name__ == "__main__":
    unittest.main()
