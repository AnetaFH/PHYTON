# PROJEKT 1 - TEXTOVÝ ANALYZÁTOR
## projekt_1_hlavackova.py

Toto je první projekt pro Engeto Online Python Akademii.

## Autor
**Aneta Flachs (Hlaváčková)**  
Email: aneta.hlavackova@skanska.cz

## Popis
Tento skript provádí různé úkoly analýzy textu, včetně:
- Kontrola, zda je hodnota v seznamu
- Počítání výskytů slov v textu
- Hledání pěti nejčastějších slov
- Zobrazení sloupcového grafu délek slov
- Počítání slov začínajících velkými písmeny
- Počítání slov psaných velkými písmeny
- Počítání slov psaných malými písmeny
- Počítání čísel v textu
- Sčítání všech čísel v textu

## Použití
1. **Importujte požadovaný modul:**
   ```python
   from task_template import TEXTS
Definujte funkce pro analýzu textu:

je_hodnota_v_seznamu(hodnota, seznam): Kontroluje, zda je hodnota v seznamu.\
pocet_vyskytu_slov(text): Počítá výskyty slov v textu.\
pet_nej_vyskytu(slovnik): Hledá pět nejčastějších slov.\
slovnik_do_grafu(slovnik): Zobrazuje sloupcový graf délek slov.\
pocet_slov_zVp(text): Počítá slova začínající velkými písmeny.\
pocet_slov_velkaP(text): Počítá slova psaná velkými písmeny.\
pocet_slov_malaP(text): Počítá slova psaná malými písmeny.\
pocet_cisel(text): Počítá čísla v textu.\
cisla(text): Vrací seznam čísel v textu.\
suma_cisel(cisla): Sčítá všechna čísla v textu.\
vygeneruj_jednotliva_slova(texts): Generuje jednotlivá slova z textů, očištěná o nežádoucí znaky.

Hlavní část programu:

Registrovat uživatele a hesla.
Vyžádat si přihlašovací údaje uživatele.
Umožnit uživateli vybrat text k analýze.
Provést různé úkoly analýzy textu a zobrazit výsledky.
