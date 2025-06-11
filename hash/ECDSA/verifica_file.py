from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization

# Carica chiave pubblica
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Carica messaggio e firma
with open("messaggio.txt", "rb") as f:
    messaggio = f.read()
with open("firma.bin", "rb") as f:
    firma = f.read()

# Verifica la firma
try:
    public_key.verify(firma, messaggio, ec.ECDSA(hashes.SHA256()))
    print("Firma verificata correttamente!")
except Exception as e:
    print("Firma non valida!", e)
