'''
moja_lista = []
moja_lista.append(10)
moja_lista.append(20)
moja_lista.append(30)

print(moja_lista)
print(moja_lista[1])

print(moja_lista[0:2])

moja_lista.remove(20)
print(moja_lista)


voce = ["jabuka", " banana "," kruska"]
print(voce[0])
voce.append("naranca")
print(voce)

# Ovo je 2D lista (3 retka, 3 stupca)
ormar = [
    ['majica', 'kapa', 'sal'],    # 0. redak (polica)
    ['hlace', 'carape', 'remen'], # 1. redak
    ['jakna', 'cipele', 'cizme']  # 2. redak
]

print(ormar[1])
print(ormar[1][1])
for redak in ormar:
    print(redak[1])

def pronadji_broj (lista, trazeni_broj):
    for broj in lista:
        if broj == trazeni_broj:
            provjera = True
            break
        else:
            provjera = False

    if provjera:
        print(f"Broj {trazeni_broj} je na listi.")
    else:
         print(f"Broj {trazeni_broj} nije na listi.")

provjera = False

lista_brojeva = [10, 20, 30, 40, 50]
trazeni_broj = 30

pronadji_broj(lista_brojeva, trazeni_broj)


rezultati = [('hlapić', 15), ('gita', 12), ('majstor', 10)]
tablica = [['Riječ', 'Frekvencija']]
for rijec in rezultati:
    tablica.append(list(rijec))
for redak in tablica:
    print(redak)
'''