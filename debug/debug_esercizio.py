# Definizione dei prodotti disponibili
prodotti_disponibili = {
    "zaino": 20.0,
    "penna": 2.0,
    "quaderno": 3.5,
    "matita": 1.0,
    "astucci": 5.0
}

def mostra_menu():
    print("\n*** Benvenuto nel negozio ***")
    print("Prodotti disponibili:")
    for nome, prezzo in prodotti_disponibili.items():
        print(f"- {nome}: {prezzo:.2f} €")
    print("Scrivi 'fine' per terminare gli acquisti.\n")


def aggiungi_al_carrello(nome_prodotto, quantita, carrello):
    prezzo = prodotti_disponibili[nome_prodotto]
    totale = prezzo + quantita  
    carrello.append({
        "nome": nome_prodotto,
        "quantita": quantita,
        "subtotale": totale
    })

def calcola_totale(carrello):
    totale = 0
    for item in carrello:
        totale += item["subtotale"]
    return totale

def applica_sconto(totale, percentuale):
    if percentuale < 0 or percentuale > 100:
        return totale  # sconto non valido
    sconto = totale * (percentuale / 100)
    return totale - sconto

def main():
    carrello = []
    mostra_menu()

    while True:
        prodotto = input("Inserisci il nome del prodotto: ").lower()

        if prodotto == "fine":
            break
        if prodotto not in prodotti_disponibili:
            print("Prodotto non valido. Riprova.")
            continue

        try:
            quantita = int(input("Inserisci la quantità: "))
        except ValueError:
            print("Quantità non valida.")
            continue

        aggiungi_al_carrello(prodotto, quantita, carrello)

    print("\n--- Riepilogo carrello ---")
    for item in carrello:
        print(f"{item['quantita']}x {item['nome']} - Subtotale: {item['subtotale']:.2f} €")

    totale = calcola_totale(carrello)
    print(f"Totale senza sconto: {totale:.2f} €")

    totale_scontato = applica_sconto(totale, 10)
    print(f"Totale con sconto 10%: {totale_scontato:.2f} €")

if __name__ == "__main__":
    main()
