from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization

# Carica chiave privata
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

# Carica chiave pubblica
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Messaggio
messaggio = b"Firma con chiavi salvate su file"

# Firma
firma = private_key.sign(messaggio, ec.ECDSA(hashes.SHA256()))

# Verifica
try:
    public_key.verify(firma, messaggio, ec.ECDSA(hashes.SHA256()))
    print("Verifica riuscita!")
except Exception as e:
    print("Verifica fallita!", e)
