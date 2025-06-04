def genera_ricevuta(prodotti, totale_finale):
    print("=== RICEVUTA ===")
    for nome, prezzo, quantita in prodotti:
        print(f"{nome}: {quantita} x {prezzo}€")
    print(f"Totale con sconto: {totale_finale:.2f}€")
