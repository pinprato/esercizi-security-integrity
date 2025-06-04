import unittest
from login import login

class TestLogin(unittest.TestCase):

    def test_accesso_ok(self):
        self.assertEqual(login("admin", "1234"), "Accesso consentito")

    def test_password_errata(self):
        self.assertEqual(login("admin", "0000"), "Accesso negato")

    def test_username_errato(self):
        self.assertEqual(login("user", "1234"), "Accesso negato")

    def test_username_maiuscolo(self):
        self.assertEqual(login("Admin", "1234"), "Accesso negato")

if __name__ == '__main__':
    unittest.main()

'''
Ogni def test_xxx è un test automatico

assertEqual controlla se il risultato è quello che ci aspettiamo

Se qualcosa fallisce, ci dice esattamente dove
'''