"""
main.py: třetí projekt do Engeto Online Python Akademie
author: Aneta Flachs (Hlavackova)
email: aneta.hlavackova@skanska.cz
"""
import sys
import requests
from bs4 import BeautifulSoup as bs
import csv
from urllib.parse import urljoin



# FUNKCE
# fce k ověření, že uživatel zadal 2 argumenty a ve správném pořadí
# (nezapomeň, že sys započítává jako první argument vždy název souboru)
def overeni_argumentu(url, jmeno_csv):
    # Pokud argumenty jsou → použij je
    if len(sys.argv) == 3:
        url = sys.argv[1]
        jmeno_csv = sys.argv[2]
        print(f"Argumenty z příkazové řádky: URL={url}, soubor={jmeno_csv}")

    else:
        # Pokud chybí → zeptej se uživatele
        print("Argumenty nebyly zadány, zadejte je ručně:")
        url = input("Zadejte URL (např. https://www.volby.cz/...): ").strip()
        jmeno_csv = input("Zadejte název souboru (např. vysledky.csv): ").strip()

    # Ověř URL
    if not url.startswith("https://www.volby.cz/"):
        print("Chyba: URL musí být z domény www.volby.cz!")
        sys.exit(1)

    return url, jmeno_csv

# fce, která nám načte obsah url stránky
def nacti_obsah_stranky(url):
    try:
       # zadej požadavek na zadanou URL
       response = requests.get(url)
       response.encoding = "utf-8-sig"

       if response.ok:
          # Parsuj HTML pomocí BeautifulSoup
          soup = bs(response.text, "html.parser")
          print("Načítám zadané url.")
          return soup
       
    except:
        # pokud není ok, vrať None
        return None

# # fce, která nám vrátí odkazy na jednotlivé obce a sesbírá data
# obci Benesova
def get_obec_links(soup, base_url):
    links = []
    nazvy_obci = []
    id_obci = []

    # najdi všechny tabulky
    tables = soup.find_all("table", {"class": "table"})

    # první for: sbírej odkazy
    for table in tables:
        trs = table.find_all("tr")[2:]  # přeskoč hlavičku
        for tr in trs:
            td_cislo = tr.find("td", {"headers": lambda h: h and "sa1" in h})
            if td_cislo and td_cislo.a:
                href = td_cislo.a.get("href")
                if href:
                    full_url = urljoin(base_url, href)
                    links.append(full_url)

    # druhý bod: sbírej názvy obcí
        
            td_nazev = tr.find("td", {"class": "overflow_name"})
            if td_nazev:
                nazev = td_nazev.get_text(strip=True)
                nazvy_obci.append(nazev)

    # třetí bod: sbírej kódy obcí
            td_id_obce = tr.find("td", {"class": "cislo"})
            if td_id_obce:
                id_o = td_id_obce.get_text(strip=True)
                id_obci.append(id_o)             

    # # Debug výpis
    # print("Nalezené URL adresy:")
    # for link in links:
    #     print(link)
    return links, nazvy_obci, id_obci


# fce, která načte obsah webů hlasování obcí a sesbírá data o výsledcích hlasování, , tu pak vnoříme do fce, která nám projde všechny linky
def nacti_obsah_kod_obce(url):
    # nejdříve načteme linky jednotlivých obcí
    try:
       # zadej požadavek na zadanou URL
       response = requests.get(url)
       response.encoding = "utf-8-sig"

       if response.ok:
          # Parsuj HTML pomocí BeautifulSoup
          soup = bs(response.text, "html.parser")
          return soup
       
    except:
        # pokud není ok, vrať None
        return None


# fce, která nám načte všechny obsahy v links
def nacti_obsah_HTML_obci(links):
    all_soup = []

    for url in links:
        soup = nacti_obsah_kod_obce(url)
        if soup:
            all_soup.append(soup)    
    return all_soup


def get_vysledky_hlasovani_obci(all_soup):
    nazvy_stran = []
    vsechny_vysledky = []
    obec_vysledky_v = []
    obec_vysledky_e = []
    obec_vysledky_r = []

    for i, soup in enumerate(all_soup):
        # čati všechny tabulky
        tables = soup.find_all("table", {"class": "table"})

        strany_vysledky = []

        # projdi všechny tables v tabulkách
        for table in tables:
            trs = table.find_all("tr")[2:]  # přeskoč hlavičku

            # projdi všechny řádky v tables
            for tr in trs:
                # sbírej všechny názvy stran
                if i == 0:
                    td_strana = tr.find("td", {"class": "overflow_name"})
                    if td_strana:
                        nazev = td_strana.get_text(strip=True)
                        nazvy_stran.append(nazev)
                
                # sbírej všechny hlasy stran
                td_hlasu = tr.find("td", {"headers": lambda h: h and h.startswith("t") and "sb3" in h})
                if td_hlasu:
                    hlasu = td_hlasu.get_text(strip=True)
                    strany_vysledky.append(hlasu)
                
                # sbírej celkové hlasy v obci valid
                td_obec_v = tr.find("td", {"headers": lambda h: h and "sa6" in h})
                if td_obec_v:
                    hlasu_o_v = td_obec_v.get_text(strip=True)
                    obec_vysledky_v.append(hlasu_o_v)

                # sbírej celkové hlasy v obci enveloped
                td_obec_e = tr.find("td", {"headers": lambda h: h and "sa5" in h})
                if td_obec_e:
                    hlasu_o_e = td_obec_e.get_text(strip=True)
                    obec_vysledky_e.append(hlasu_o_e)

                # sbírej celkové hlasy v obci registered
                td_obec_r = tr.find("td", {"headers": lambda h: h and "sa5" in h})
                if td_obec_r:
                    hlasu_o_r = td_obec_r.get_text(strip=True)
                    obec_vysledky_r.append(hlasu_o_r)

        vsechny_vysledky.append(strany_vysledky)

    return nazvy_stran, vsechny_vysledky, obec_vysledky_v, obec_vysledky_e, obec_vysledky_r
    
    



    

    

# # fce, která nám zapíše jednotlivé obce do .csv souboru
def zapis_csv(
        nazev_csv,
        nazvy_obci,
        id_obci,
        nazvy_stran,
        vysledky_stran,
        obec_vysledky_v,
        obec_vysledky_e,
        obec_vysledky_r
        ):
    with open(nazev_csv, mode= "w", newline= "", encoding= "utf-8-sig") as f:
        writer_1 = csv.writer(f, delimiter=";")
        # zapiš hlavičku
        header = ["code", "location", "registered", "envelopes", "valid"] + list(nazvy_stran)
        writer_1.writerow(header)

        # zapis každého id, název obce do nového řádku
        for code_o, nazev, obec_hlasy_r, obec_hlasy_e, obec_hlasy_v, strany in zip(id_obci, nazvy_obci, obec_vysledky_r, obec_vysledky_e, obec_vysledky_v, vysledky_stran):
            radek = [code_o, nazev, obec_hlasy_r, obec_hlasy_e, obec_hlasy_v] + list(strany)
            writer_1.writerow(radek)


    print(f"Zapisuji .csv souboru {nazev_csv} a ukládám jej.")



# # fce, která nám vrátí odkazy na jednotlivé obce
# obci Benesova 

# # # fce, která vytvoří csv soubor a zapíše do něj názvy obcí

    



def main():
    url, soubor_csv = overeni_argumentu(None, None)    
    print(f'ok URL: {url}')
    print(f'ok Výstupní soubor: {soubor_csv}')

    if not soubor_csv.endswith(".csv"):
        soubor_csv += ".csv"


    obsah_url = nacti_obsah_stranky(url)
    if obsah_url is None:
        print('Nedostupný HTML objekt.')
        return None

    # Dál pokračuješ...
    print('Vše OK, pokračujeme!')

    obce_link, nazvy_obci, id_obci = get_obec_links(obsah_url, url)
    print(f"Nalezeno {len(obce_link)} obcí. Stahuji data z vybraneho URL: {url}")
    
    vsechny_html = nacti_obsah_HTML_obci(obce_link)

    nazvy_stran, vysledky_stran_obci, envelope, registered, celkove_vysledky  = get_vysledky_hlasovani_obci(vsechny_html)
        
    zapis_csv(
        soubor_csv,
        nazvy_obci,
        id_obci,
        nazvy_stran,
        vysledky_stran_obci,
        celkove_vysledky,
        envelope,
        registered
        )
if __name__=='__main__':
    main()