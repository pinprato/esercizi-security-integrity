import hashlib
input_hash = input("Enter the hash to validate: ")

if input_hash == hashlib.md5(b"password").hexdigest():
    print("Hash is valid.")
else:
    print("Hash is invalid.")
# Compare this snippet from hash/validate_hash.py: