import sys
import requests
#from lxml import html
from bs4 import BeautifulSoup


#url = "https://www.ef.jcu.cz"

def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []
    response = requests.get(url)
    if response.status_code == 200:
        html_file = response.text
        soup = BeautifulSoup(html_file, "html.parser")
        #print(soup)
        all_a = soup.find_all("a")
        #print(all_a)
        for one_a in all_a:
            item = one_a.get("href")
            #print(item)
            hrefs.append(item) 
            #print(hrefs)      
    return hrefs

#download_url_and_get_all_hrefs(url)


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        download_url_and_get_all_hrefs(url)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
