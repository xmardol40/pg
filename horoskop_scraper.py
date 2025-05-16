import requests
from bs4 import BeautifulSoup

def ziskej_popis_znameni():
    znameni = [
        "beran", "byk", "blizenci", "rak", "lev", "panna",
        "vahy", "stir", "strelec", "kozoroh", "vodnar", "ryby"
    ]

    popisy = {}

    for z in znameni:
        url = f"https://www.horoskopy.cz/{z}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            odstavce = soup.find_all("p")
            if odstavce:
                # Spojíme všechny <p> prvky do jednoho textu, každý očistíme stripem
                text = "\n".join(p.get_text(strip=True) for p in odstavce)
                popisy[z] = text
                #print(popisy)
            else:
                popisy[z] = "Popis nebyl nalezen."

        except Exception as e:
            popisy[z] = f"Chyba při načítání ({z}): {str(e)}"

    return popisy

# Test: výpis výsledného slovníku
#if __name__ == "__main__":
#    data = ziskej_popis_znameni()
#    for znameni, popis in data.items():
#        print(f"{znameni}:\n{popis}\n")

#    print(data)
