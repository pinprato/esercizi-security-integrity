import unittest
from convertitore import converti_euro_in_dollari

class TestConvertitore(unittest.TestCase):

    def test_conversione_corretta(self):
        self.assertEqual(converti_euro_in_dollari(100), 110.00)

    def test_valore_zero(self):
        self.assertEqual(converti_euro_in_dollari(0), 0.00)

    def test_valore_negativo(self):
        self.assertGreaterEqual(converti_euro_in_dollari(-50), 0)

if __name__ == '__main__':
    unittest.main()
