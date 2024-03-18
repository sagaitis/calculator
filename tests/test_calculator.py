import unittest
from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """New instance for every test."""
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(7), 7)
        self.assertEqual(self.calc.add(-99.5), -92.5)

    def test_subtract(self):
        # Start with 99 in memory.
        self.calc.add(99)

        self.assertEqual(self.calc.subtract(147), -48)
        self.assertEqual(self.calc.subtract(-19), -29)

    def test_multiply(self):
        self.calc.add(-50)

        self.assertEqual(self.calc.multiply(2), -100)
        self.assertEqual(self.calc.multiply(-1), 100)
        self.assertEqual(self.calc.multiply(0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2), 0)

        self.calc.add(15)
        self.assertEqual(self.calc.divide(-2), -7.5)

        # Division by zero
        self.assertIsNone(self.calc.divide(0))

    def test_root(self):
        self.calc.add(16)
        self.assertEqual(self.calc.root(2), 4)
        self.calc.reset()

        self.calc.add(64)
        self.assertAlmostEqual(self.calc.root(3), 4, places=5)

    def test_reset(self):
        self.calc.add(5)
        self.calc.reset()
        self.assertEqual(self.calc.memory, 0)


if __name__ == '__main__':
    unittest.main()
