from modulo_prezzi import calcola_totale
from modulo_sconti import applica_sconto
from modulo_ricevuta import genera_ricevuta

def test_integrazione_ordine():
    prodotti = [
        ("Zaino", 25, 2),
        ("Penna", 2, 10),
        ("Quaderno", 5, 5)
    ]
    totale = calcola_totale(prodotti)
    totale_scontato = applica_sconto(totale)
    genera_ricevuta(prodotti, totale_scontato)

if __name__ == "__main__":
    test_integrazione_ordine()
