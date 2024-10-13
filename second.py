jednociferna_cisla = {
    "0": "",
    "1": "jedna",
    "2": "dva",
    "3": "tři",
    "4": "čtyři",
    "5": "pět",
    "6": "šest",
    "7": "sedm",
    "8": "osm",
    "9": "devět",
    "10": "deset"}

dvouciferna_cisla_do_19 = {
    "1": "jede",
    "2": "dva",
    "3": "tři",
    "4": "čtr",
    "5": "pat",
    "6": "šest",
    "7": "sedm",
    "8": "osm",
    "9": "devate"}

dvouciferna_cisla_do_99 = {
    "5": "pa",
    "6": "še",
    "7": "sedm",
    "8": "osm",
    "9": "deva"} 
nact = "náct"
deset = "cet "
desat = "desát "

def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    #return "dvacet pět"
    if int(cislo) == 0:
        return "nula"
    if 0 < int(cislo) <= 10:
        return jednociferna_cisla[cislo]
    elif 10 < int(cislo) < 20:
        return f"{dvouciferna_cisla_do_19[cislo[1]]+nact}"        
    elif 20 <= int(cislo) < 50:
        return f"{jednociferna_cisla[cislo[0]]+deset +jednociferna_cisla[cislo[1]]}"   
    elif 50 <= int(cislo) < 100:
        return f"{dvouciferna_cisla_do_99[cislo[0]]+desat+jednociferna_cisla[cislo[1]]}"  
    elif int(cislo) == 100:
        return "100"
    else:
        return f"Toto číslo není v rozsahu 0 - 100"   

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)