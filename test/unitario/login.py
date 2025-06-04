a="ciao"

def login(username, password):
    if username == "admin" and password == "1234":
        return "Accesso consentito"
    else:
        return "Accesso negato"

# Test manuale
print(login("admin", "1234"))   # Deve stampare "Accesso consentito"
print(login("admin", "0000"))   # Deve stampare "Accesso negato"
a=12
print(login("Admin", "1234"))   # Deve stampare "Accesso negato"
print(a)


''' 
Provare a cambiare utente/password

Trovare cosa succede se si usa "Admin" al posto di "admin"

Provare a mettere None, numeri, ecc.

'''