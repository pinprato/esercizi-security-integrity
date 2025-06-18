import mysql.connector
import hashlib

try:
    # Connessione al database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",  # Metti qui la tua password MySQL se c'è
        database="testDB"  # Nome del database che stai usando
    )
    print(" Connessione al database riuscita!")

except mysql.connector.Error as err:
    print(f" Errore di connessione al database: {err}")
    exit(1)  # Interrompe il programma

# Crea il cursore
cursor = conn.cursor()

# Input utente e password
email = input("Email: ").strip()
password = input("Password: ").strip()

# Calcolo SHA-256 della password
password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

print(f"Password hash calcolato: {password_hash}")

# Query di verifica
query = "SELECT * FROM utenti WHERE email=%s AND pwd=%s"

try:
    cursor.execute(query, (email, password_hash))
    result = cursor.fetchone()
    print(result)
    if result:
        print("Accesso consentito!")
    else:
        print("Accesso negato!")

except mysql.connector.Error as err:
    print(f"Errore nell'esecuzione della query: {err}")

# Chiudi il cursore e la connessione
cursor.close()
conn.close()
print("Connessione chiusa.")
