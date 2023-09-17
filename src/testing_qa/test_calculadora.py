import unittest
import calculadora

class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(calculadora.suma(3, 5), 8)
        self.assertEqual(calculadora.suma(-1, 1), 0)
        self.assertEqual(calculadora.suma(-1, -1), -2)

    def test_resta(self):
        self.assertEqual(calculadora.resta(10, 5), 5)
        self.assertEqual(calculadora.resta(-1, 1), -2)
        self.assertEqual(calculadora.resta(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()