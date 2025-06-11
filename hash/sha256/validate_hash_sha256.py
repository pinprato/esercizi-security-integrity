import hashlib
input_hash = input("Enter the hash to validate: ")

if input_hash == hashlib.sha256(b"Ciao").hexdigest():
    print("Hash is valid.")
else:
    print("Hash is invalid.")
# Compare this snippet from hash/validate_hash.py: