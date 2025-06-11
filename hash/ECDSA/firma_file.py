from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization

# Carica chiave privata
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# Carica messaggio da file
with open("messaggio.txt", "rb") as f:
    messaggio = f.read()

# Firma il messaggio
firma = private_key.sign(messaggio, ec.ECDSA(hashes.SHA256()))

# Salva la firma
with open("firma.bin", "wb") as f:
    f.write(firma)

print("Firma salvata in firma.bin")
