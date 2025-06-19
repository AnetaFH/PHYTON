# Elections Scraper — Třetí projekt do Engeto Online Python Akademie

**Autor:** Aneta Flachs (Hlavackova)  
**Email:** aneta.hlavackova@skanska.cz

---

## Popis projektu

Tento Python projekt je scraper, který stahuje a ukládá výsledky voleb do Poslanecké sněmovny Parlamentu ČR z roku 2017 z portálu [www.volby.cz](https://www.volby.cz).

Program:
- **ověří správnost argumentů**
- stáhne výsledky hlasování všech obcí vybraného územního celku
- uloží je do přehledného CSV souboru

Výstupní soubor má pro každou obec:
- kód obce
- název obce
- registrované voliče
- vydané obálky
- platné hlasy
- hlasy pro každou kandidující stranu

---

## Instalace knihoven

Projekt je spuštěn ve **virtuálním prostředí** `env_projekt_3`.

1) **Aktivace prostředí:**

```bash
.\env_projekt_3\Scripts\Activate
```

2) **Instalace knihoven:**

```bash
pip install -r requirements.txt
```

Knihovny jsou exportovány pomocí:
```bash
pip freeze > requirements.txt
```

---

## Spuštění projektu

Skript vyžaduje **2 argumenty**:
1. URL odkazu na výběr obcí
2. Název výstupního souboru (např. `vysledky_benesov.csv`)

**Syntaxe:**

```bash
python main.py "<URL>" <vystup.csv>
```

---

## Ukázka

### Použitý příklad:

- **URL:**  
  `https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101`  
  _(okres Benešov)_

- **Výstupní soubor:**  
  `vysledky_benesov.csv`

### Postup:

1) Aktivuj prostředí:  
```bash
.\env_projekt_3\Scripts\Activate
```

2) Spusť scraper:  
```bash
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" vysledky_benesov.csv
```

3) Po úspěšném stažení otevři soubor `vysledky_benesov.csv` v Excelu nebo jiném tabulkovém editoru.

---

## Struktura projektu

```
projekt_3/
├── env_projekt_3/          # Virtuální prostředí (na GitHub NENAHRÁVAT)
├── main.py                 # Hlavní scraper
├── requirements.txt        # Seznam knihoven
├── vysledky_benesov.csv    # Výstupní CSV (po spuštění)
└── README.md               # Tento soubor
```

---

## Důležitá poznámka

Při spouštění v **PowerShellu** vždy použij **single quotes `' '`**, pokud URL obsahuje znak `&`:
```bash
python main.py 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101' vysledky_benesov.csv
```

---

## Hotovo!

Děkuji za přečtení!
**Dotazy:** aneta.hlavackova@skanska.cz
