def conta_parole(testo):
    parole = testo.split(" ")
    return len(parole)

# Bug: non rimuove punteggiatura, quindi "ciao," è diverso da "ciao"
