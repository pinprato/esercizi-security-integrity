#pip install cryptography

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# 1. Genera coppia di chiavi
private_key = ec.generate_private_key(ec.SECP256K1())
public_key = private_key.public_key()

# 2. Messaggio da firmare
messaggio = b"Ciao Marco, questa e una firma digitale"

# 3. Firma digitale
firma = private_key.sign(messaggio, ec.ECDSA(hashes.SHA256()))

# 4. Verifica firma
try:
    public_key.verify(firma, messaggio, ec.ECDSA(hashes.SHA256()))
    print("Firma verificata con successo!")
except Exception as e:
    print("Firma NON valida!", e)


# Modifico anche solo 1 lettera
messaggio_modificato = b"Ciao Marco, questa e una firma digitalE"

try:
    public_key.verify(firma, messaggio_modificato, ec.ECDSA(hashes.SHA256()))
    print("Firma verificata anche con messaggio modificato!")
except Exception as e:
    print("ATTENZIONE: firma non valida dopo modifica!", e)