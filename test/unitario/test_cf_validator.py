import unittest
from cf_validator import valida_codice_fiscale

class TestCFValidator(unittest.TestCase):

    def test_cf_valido(self):
        self.assertTrue(valida_codice_fiscale("RSSMRA85M01H501Z"))

    def test_cf_troppo_corto(self):
        self.assertFalse(valida_codice_fiscale("RSSMRA85"))

    def test_cf_con_simboli(self):
        self.assertFalse(valida_codice_fiscale("RSSMRA85M01H@01Z"))

    def test_cf_troppo_lungo(self):
        self.assertFalse(valida_codice_fiscale("RSSMRA85M01H501ZZZ"))

if __name__ == '__main__':
    unittest.main()
