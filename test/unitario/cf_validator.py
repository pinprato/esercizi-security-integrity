def valida_codice_fiscale(cf):
    # Codice fiscale fittizio = 16 caratteri alfanumerici
    if len(cf) != 16:
        return False
    if not cf.isalnum():
        return False
    return True
