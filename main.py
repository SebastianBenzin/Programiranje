def ucitaj_tekst(filepath):
    try:
    #ovdje ide logika za čitanje datoteke
        with open (filepath,'r',encoding='utf-8') as file:
         sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f'greška: Datoteka na putanji {filepath} ne postoji.')
        return None #vraća prazan skup podataka, ako ne nađe datoteku

#Funkcija koja prociscava tekst
def ocisti_tekst(tekst):
    #ovdje ide logika za pročišćavanje teksta
    tekst = tekst.lower()
    interpunkcija = ['.',',','!','?',':',';','"',"'",'(',')']
    for znak in interpunkcija:
        tekst = tekst.replace(znak, '')
    lista_rijeci = tekst.split()
    return lista_rijeci






def broji_frekvenciju(lista_rijeci):
     # 1. Kreiramo prazan rječnik koje će čuvati rezultate
    rjecnik_frekvencije = {}

    # 2. Prolazimo kroz svaku riječ i primljenoj listi
    for rijec in lista_rijeci:
        if rijec in rjecnik_frekvencije:
            rjecnik_frekvencije[rijec] +=1
        else:
            rjecnik_frekvencije[rijec] = 1
    return rjecnik_frekvencije

#čišćenje teksta od veznika i sličnih "nebitnih" riječi
def ukloni_stop_words(rjecnik_frekvencije, stop_words_lista):
    ocisceni_rjecnik = {}
    for rijec, frekvencija in rjecnik_frekvencije.items():
        if rijec not in stop_words_lista:
            ocisceni_rjecnik[rijec] = frekvencija
    return ocisceni_rjecnik

STOP_WORDS = ['i', 'u', 'na', 'je', 'se', 'su', 's', 'za', 'o', 'a', 'pa', 'te', 'li', 'da', 'ali', 'bi', 'bio', 'bila', 'što', 'ga', 'mu', 'joj', 'ih']


    
   

#glavni dio programa
if __name__ == '__main__':
    filepath = 'tekst.txt'
    print(f'učitavam tekst iz datoteke :{filepath}')

    ucitani_tekst = ucitaj_tekst(filepath)

    if ucitani_tekst:
        print('\ntekst uspješno učitan. slijedi ispis sadržaja:')
        print('-' * 40)
        print(ucitani_tekst)
        print('-' * 40)
    else:
        print('program se prekida jer tekst nije učitan.')
    procisceni_tekst = ocisti_tekst(ucitani_tekst)
    if procisceni_tekst:
        print("Pročišćeni tekst je:")
        print('-' * 40)
        print(procisceni_tekst)
        print('-' * 40)
    else:
        print("program se prekida jer tekst nije pročišćen")
    
    # NOVI DIO - POZIVAMO NOVU FUNKCIJU
    print("Brojim frekvenciju riječi...")
    broj_rijeci = broji_frekvenciju(procisceni_tekst)
    print("Brojanje završeno")

    #Ispisujemo rezultat da vidim što smo dobili
    print("\n--- Rječnik frekvencije ---")
    print(broj_rijeci)
    print("---------------------------")
    
    # Faza 3: filtriranje i sortiranje
    ociscene_frekvencije = ukloni_stop_words(broj_rijeci, STOP_WORDS)
    print("\n--- očišćeni rječnik frekvencije ---")
    print(ociscene_frekvencije)
    print("---------------------------")

else:
    print("program se prekida jer tekst nije pročišćen")

    

