"""
projekt_1_hlavackova.py: prvni projekt do Engeto Online Python Akademie

author: Aneta Flachs (Hlavackova)
email: aneta.hlavackova@skanska.cz
"""
# TODO: importujeme pythonovy soubor 'task_template.py' s texty do aktualniho souboru
from task_template import TEXTS

# urci zda je hodnota v seznamu
def je_hodnota_v_seznamu(hodnota, seznam):
       return hodnota in seznam

# vyskyt slov v textu
def pocet_vyskytu_slov(text):
       pocet_vyskytu = {}
       for slovo in text:
              if slovo.lower() not in pocet_vyskytu:
                     pocet_vyskytu[slovo.lower()] = 1
              else:
                     pocet_vyskytu[slovo.lower()] += 1
       return pocet_vyskytu

# hledame pet nejcastejsich
def pet_nej_vyskytu(slovnik):
       pet_nej_hodnot = ()
       pet_nej_hodnot = sorted(list(slovnik.values()), reverse=True)[:5]
       for vyskyt in slovnik:
              if slovnik[vyskyt] in pet_nej_hodnot:
                     pet_nej_hodnot.remove(slovnik[vyskyt])
                     pet_nej_hodnot.append((slovnik[vyskyt], vyskyt))
       return pet_nej_hodnot

# zobrazime sloupcovy graf prezentujici cetnost ruznych delek slov v textu
def slovnik_do_grafu(slovnik):
       oddelovac_graf = "|--|------------|--|"
       for index, par in enumerate(sorted(slovnik, reverse=True), 1):
              print(oddelovac_graf, f"|{index}.|{par[1]: ^12}|{par[0]}x|", oddelovac_graf, sep="\n")

# počet slov začínajích velkými písmeny  
def pocet_slov_zVp(text):
       pocet_slov_Vp = 0
       for slovo in text:
              if slovo[0].istitle():
                     pocet_slov_Vp += 1
       return pocet_slov_Vp

# počet slov psaných velkými písmeny
def pocet_slov_velkaP(text):
       pocet_velkaP = 0
       for slovo in text:
              if slovo.isupper():
                     pocet_velkaP += 1
       return pocet_velkaP

# počet slov psaných malými písmeny
def pocet_slov_malaP(text):
       pocet_malaP = 0
       for slovo in text:
              if slovo.islower():
                     pocet_malaP += 1
       return pocet_malaP

# funkce, ktera vraci pocet cisel v textu
def pocet_cisel(text):
       pocet = 0
       for slovo in text:
              if slovo.isdigit():
                     pocet += 1
       return pocet

# vraci seznam cisel v textu
def cisla(text):
       seznam_cisel = []
       for slovo in text:
              if slovo.isdigit():
                     seznam_cisel.append(slovo)
       return seznam_cisel

# vraci sumu všech cisel, která vstupuji do funkce jako seznam cisel
def suma_cisel(cisla):
       suma = 0
       for cislo in cisla:
              suma += int(cislo)
       return suma

# vygeneruje jednotliva slova z texts, ocisteno o nechtene znaky
def vygeneruj_jednotliva_slova(texts):
       jednotliva_slova = []
       for slovo in texts[(vybrane_cislo_textu)-1].split():
              ciste_slovo = slovo.strip('.,!<>?:')
              jednotliva_slova.append(ciste_slovo)
       return jednotliva_slova
 
# MAIN #
# TODO: do pameti zapiseme registrovane uzivatele s hesly jako listy, ktere propojim do slovniku:
user = ["bob", "ann", "mike", "liz"]
password = ["123", "pass123", "password123", "pass123"]
slovnik_reg_uzivatele = dict(zip(user, password))
oddelovac = "-"

# TODO: program si vyzada prihlasovaci udaje uzivatele: jmeno a heslo
uzivatel = input("Zadejte jmeno: ")
# TODO: zkontroluje, zda je uzivatel registrovany, pokud neni, program se rozlouci a ukonci
if not uzivatel in user:
        print("Bohuzel, zadany uzivatel neexistuje!")
        quit()
# TODO: pokud je uzivatel registrovany, musi zadat heslo
else:
        print("V poradku ")
        # # print(slovnik_reg_uzivatele[uzivatel])
        heslo = input("Zadejte heslo: ")
        if heslo != (slovnik_reg_uzivatele[uzivatel]):
                print("Bohuzel, heslo je spatne!")
                quit()
        # pokud uzivatel existuje a zadal spravne heslo, umozni mu program analyzovat texty
        else:
              print("V poradku. Vitej v aplikaci " + uzivatel + "!")

print(55 * oddelovac)

# TODO: dame uzivateli vybrat cislo, kterym vybere text pro analyzu
moznosti = [1, 2, 3]
vybrane_cislo_textu = int(input("Zadejte cislo od 1 do 3, vyberete tim text k analyze: "))

if je_hodnota_v_seznamu(vybrane_cislo_textu, moznosti):
       print(f"Zvolili jste text cislo {vybrane_cislo_textu}.")
       print((TEXTS[(vybrane_cislo_textu)-1]), sep='\n')
else:
       print("Zadany text neexistuje!")
       quit()
       
print(55 * oddelovac)
    
# TOTO JE HLAVNI CAST PROGRAMU

# TODO: pro vybrany text spocita nasledujici statistiky
jednotliva_slova = vygeneruj_jednotliva_slova(TEXTS)

print(f'Pocet slov v textu je: {len(jednotliva_slova)}.')
print(f"Pocet vyskytu slov: {pocet_vyskytu_slov(jednotliva_slova)}")
print(f"Pocet slov zacinajicich velkym pismenem je v textu {pocet_slov_zVp(jednotliva_slova)}")
print(f"Pocet slov psanych velkymi pismeny je v textu {pocet_slov_velkaP(jednotliva_slova)}")
print(f"Pocet slov psanych malymi pismeny je v textu {pocet_slov_malaP(jednotliva_slova)}")
print(f"Pocet cisel v textu je {pocet_cisel(jednotliva_slova)}")
print(f"Cisla v textu jsou {cisla(jednotliva_slova)}")
print(f"Soucet cisel v textu je {suma_cisel(cisla(jednotliva_slova))}")
print(f"Pet nejcastejsich slov jsou {pet_nej_vyskytu(pocet_vyskytu_slov(jednotliva_slova))}")

print(55 * oddelovac)

slovnik_do_grafu(pet_nej_vyskytu(pocet_vyskytu_slov(jednotliva_slova)))