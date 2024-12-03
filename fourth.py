def moznosti_tahu(pozice, pohyby):
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
    return mozne_tahy

def neco_stoji_v_ceste(mozne_tahy, obsazene_pozice):
    for i in obsazene_pozice:
        if i in mozne_tahy:
            return True



def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Implementace pravidel pohybu pro různé figury zde.

    pohyby_1 = [(1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0)]
    pohyby_2 = [(-1,0), (-2,0), (-3,0), (-4,0), (-5,0), (-6,0), (-7,0)]
    pohyby_3 = [(0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7)]
    pohyby_4 = [(0,-1), (0,-2), (0,-3), (0,-4), (0,-5), (0,-6), (0,-7)]
    pohyby_5 = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7)]
    pohyby_6 = [(-1,1), (-2,2), (-3,3), (-4,4), (-5,5), (-6,6), (-7,7)]
    pohyby_7 = [(1,-1), (2,-2), (3,-3), (4,-4), (5,-5), (6,-6), (7,-7)]
    pohyby_8 = [(-1,-1), (-2,-2), (-3,-3), (-4,-4), (-5,-5), (-6,-6), (-7,-7)]

    if cilova_pozice[0] > 8:
        return False
    elif cilova_pozice[1] > 8:
        return False
    
    if cilova_pozice in obsazene_pozice:
        return False
    
    if figurka.get("typ") == "pěšec":
        pozice = figurka.get("pozice")
        pohyby = [(1,0), (2,0)]
        mozne_tahy = moznosti_tahu(pozice, pohyby)

        zabrana = neco_stoji_v_ceste(mozne_tahy, obsazene_pozice)
        if zabrana ==True:
            return False            
        elif cilova_pozice in mozne_tahy:
            return True
        else:
            return False
    
    elif figurka.get("typ") == "jezdec":
        pozice = figurka.get("pozice")
        pohyby = [(-1,2), (1,2),(-2,1),(2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        mozne_tahy = moznosti_tahu(pozice, pohyby)
        if cilova_pozice in mozne_tahy:
            return True
        else:
            return False
    
    elif figurka.get("typ") == "král":
        pozice = figurka.get("pozice")
        pohyby = [(-1,1), (0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
        mozne_tahy = moznosti_tahu(pozice, pohyby)
        if cilova_pozice in mozne_tahy:
            return True
        else:
            return False
        
    elif figurka.get("typ") == "věž":
        pozice = figurka.get("pozice")
        mozne_tahy_1 = moznosti_tahu(pozice, pohyby_1)
        mozne_tahy_2 = moznosti_tahu(pozice, pohyby_2)
        mozne_tahy_3 = moznosti_tahu(pozice, pohyby_3)
        mozne_tahy_4 = moznosti_tahu(pozice, pohyby_4)
        zabrana_1 = neco_stoji_v_ceste(mozne_tahy_1, obsazene_pozice)
        zabrana_2 = neco_stoji_v_ceste(mozne_tahy_2, obsazene_pozice)
        zabrana_3 = neco_stoji_v_ceste(mozne_tahy_3, obsazene_pozice)
        zabrana_4 = neco_stoji_v_ceste(mozne_tahy_4, obsazene_pozice)
    
        if cilova_pozice in mozne_tahy_1:
            if zabrana_1 == True:
                return False
            else:
                return True
        elif cilova_pozice in mozne_tahy_2:
            if zabrana_2 == True:
                return False
            else:
                return True    
        elif cilova_pozice in mozne_tahy_3:
            if zabrana_3 == True:
                return False
            else:
                return True
        elif cilova_pozice in mozne_tahy_4:
            if zabrana_4 == True:
                return False
            else:
                return True
            
    elif figurka.get("typ") == "střelec":
        pozice = figurka.get("pozice")
        mozne_tahy_5 = moznosti_tahu(pozice, pohyby_5)
        mozne_tahy_6 = moznosti_tahu(pozice, pohyby_6)
        mozne_tahy_7 = moznosti_tahu(pozice, pohyby_7)
        mozne_tahy_8 = moznosti_tahu(pozice, pohyby_8)
        zabrana_5 = neco_stoji_v_ceste(mozne_tahy_5, obsazene_pozice)
        zabrana_6 = neco_stoji_v_ceste(mozne_tahy_6, obsazene_pozice)
        zabrana_7 = neco_stoji_v_ceste(mozne_tahy_7, obsazene_pozice)
        zabrana_8 = neco_stoji_v_ceste(mozne_tahy_8, obsazene_pozice)
        
        if cilova_pozice in mozne_tahy_5:
            if zabrana_5 == True:
                return False
            else:
                return True
        elif cilova_pozice in mozne_tahy_6:
            if zabrana_6 == True:
                return False
            else:
                return True    
        elif cilova_pozice in mozne_tahy_7:
            if zabrana_7 == True:
                return False
            else:
                return True
        elif cilova_pozice in mozne_tahy_8:
            if zabrana_8 == True:
                return False
            else:
                return True

    elif figurka.get("typ") == "dáma":
        pozice = figurka.get("pozice")
        mozne_tahy_1 = moznosti_tahu(pozice, pohyby_1)
        mozne_tahy_2 = moznosti_tahu(pozice, pohyby_2)
        mozne_tahy_3 = moznosti_tahu(pozice, pohyby_3)
        mozne_tahy_4 = moznosti_tahu(pozice, pohyby_4)
        mozne_tahy_5 = moznosti_tahu(pozice, pohyby_5)
        mozne_tahy_6 = moznosti_tahu(pozice, pohyby_6)
        mozne_tahy_7 = moznosti_tahu(pozice, pohyby_7)
        mozne_tahy_8 = moznosti_tahu(pozice, pohyby_8)
        zabrana_1 = neco_stoji_v_ceste(mozne_tahy_1, obsazene_pozice)
        zabrana_2 = neco_stoji_v_ceste(mozne_tahy_2, obsazene_pozice)
        zabrana_3 = neco_stoji_v_ceste(mozne_tahy_3, obsazene_pozice)
        zabrana_4 = neco_stoji_v_ceste(mozne_tahy_4, obsazene_pozice)
        zabrana_5 = neco_stoji_v_ceste(mozne_tahy_5, obsazene_pozice)
        zabrana_6 = neco_stoji_v_ceste(mozne_tahy_6, obsazene_pozice)
        zabrana_7 = neco_stoji_v_ceste(mozne_tahy_7, obsazene_pozice)
        zabrana_8 = neco_stoji_v_ceste(mozne_tahy_8, obsazene_pozice)
        
        if cilova_pozice in mozne_tahy_1:
            if zabrana_1 == True:
                return False
            else:
                return True
        elif cilova_pozice in mozne_tahy_2:
            if zabrana_2 == True:
                return False
            else:
                return True    
        elif cilova_pozice in mozne_tahy_3:
            if zabrana_3 == True:
                return False
            else:
                return True
        elif cilova_pozice in mozne_tahy_4:
            if zabrana_4 == True:
                return False
            else:
                return True
        elif cilova_pozice in mozne_tahy_5:
            if zabrana_5 == True:
                return False
            else:
                return True
        elif cilova_pozice in mozne_tahy_6:
            if zabrana_6 == True:
                return False
            else:
                return True    
        elif cilova_pozice in mozne_tahy_7:
            if zabrana_7 == True:
                return False
            else:
                return True
        elif cilova_pozice in mozne_tahy_8:
            if zabrana_8 == True:
                return False
            else:
                return True
        


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
