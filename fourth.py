def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Implementace pravidel pohybu pro různé figury zde.

    if cilova_pozice[0] > 8:
        return False
    elif cilova_pozice[1] > 8:
        return False
    
    if cilova_pozice in obsazene_pozice:
        return False
    
    if figurka == pesec:
        pozice = figurka.get("pozice")
        pohyby = [(1,0), (2,0)]

        mozne_tahy = []

        for i in range(0,len(pohyby)):
            prvek = pohyby[i]
            tup = []
            for cislo in range(0,2):
                prvni_cislo = pozice[cislo] + prvek[cislo]
                tup.append(prvni_cislo)
                if len(tup) == 2:
                    tup = tuple(tup)
                    mozne_tahy.append(tup)
                #mozne_tahy = {(3,2),(4,2)}
        if cilova_pozice in mozne_tahy:
            return True
    
    elif figurka == jezdec:
        pozice = figurka.get("pozice")
        pohyby = [(-1,2), (1,2),(-2,1),(2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

        mozne_tahy = []

        for i in range(0,len(pohyby)):
            prvek = pohyby[i]
            tup = []
            for cislo in range(0,2):
                prvni_cislo = pozice[cislo] + prvek[cislo]
                tup.append(prvni_cislo)
                if len(tup) == 2:
                    tup = tuple(tup)
                    mozne_tahy.append(tup)
        #mozne_tahy = {(1,2),(1,4),(2,1),(2,5),(4,1),(4,5),(5,2),(5,4)}
        if cilova_pozice in mozne_tahy:
            return True
    elif figurka == dama:
        mozne_tahy = {(6,1),(7,2),(7,3),(7,4),(6,5),(5,6),(4,7),(3,8),(8,4),(8,5),(8,6),(8,7)}
        if cilova_pozice in mozne_tahy:
            return True
    elif figurka == vez:
        mozne_tahy = {(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,7),(8,6),(8,5),(8,4)}
        if cilova_pozice in mozne_tahy:
            return True
    elif figurka == kral:
        pozice = figurka.get("pozice")
        pohyby = [(-1,1), (0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]

        mozne_tahy = []

        for i in range(0,len(pohyby)):
            prvek = pohyby[i]
            tup = []
            for cislo in range(0,2):
                prvni_cislo = pozice[cislo] + prvek[cislo]
                tup.append(prvni_cislo)
                if len(tup) == 2:
                    tup = tuple(tup)
                    mozne_tahy.append(tup)
                #mozne_tahy = {(1,5),(2,5),(2,4),(2,3),(1,3)}
        if cilova_pozice in mozne_tahy:
            return True
    elif figurka == strelec:
        mozne_tahy = {(4,1), (5,2),(7,2),(8,1),(7,4),(8,5)}
        if cilova_pozice in mozne_tahy:
            return True

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
