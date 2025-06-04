import unittest
from conteggio_parole import conta_parole

class TestConteggioParole(unittest.TestCase):

    def test_frase_normale(self):
        self.assertEqual(conta_parole("ciao come va"), 3)

    def test_con_punteggiatura(self):
        self.assertEqual(conta_parole("ciao, come va? oggi"), 4)  # fallirà!

    def test_stringa_vuota(self):
        self.assertEqual(conta_parole("ciao"), 1)  # anche questo è discutibile

if __name__ == '__main__':
    unittest.main()
