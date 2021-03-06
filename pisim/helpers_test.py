import unittest
import helpers
from math import sqrt

class TestHelperFunctions(unittest.TestCase):
    def test_pythag(self):
        self.assertAlmostEqual(helpers.pythag(3, 4), 5)
        self.assertAlmostEqual(helpers.pythag(1, 1), sqrt(2))

    def test_monte_carlo_sim(self):
        self.assertAlmostEqual(helpers.monte_carlo_sim(1, 10, 20), 2)
        

    def test_get_random(self):
        self.assertTrue((helpers.get_random() > -1 and helpers.get_random() < 1))
