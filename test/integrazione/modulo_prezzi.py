def calcola_totale(prodotti):
    totale = 0
    for nome, prezzo, quantita in prodotti:
        totale += prezzo * quantita
    return totale
