def converti_euro_in_dollari(euro):
    tasso_conversione = 1.10  # 1€ = 1.10$
    dollari = euro * tasso_conversione
    return round(dollari, 2)

# Bug logico introdotto di proposito:
# Non controlliamo se euro è negativo
