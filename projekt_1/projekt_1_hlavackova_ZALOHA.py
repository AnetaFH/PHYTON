"""
projekt_1_hlavackova.py: prvni projekt do Engeto Online Python Akademie

author: Aneta Flachs (Hlavackova)
email: aneta.hlavackova@skanska.cz
"""
# TODO: do pameti zapiseme registrovane uzivatele s hesly jako listy, ktere propojim do slovniku:
user = ["bob", "ann", "mike", "liz"]
password = ["123", "pass123", "password123", "pass123"]
slovnik_reg_uzivatele = dict(zip(user, password))
oddelovac = "-"

# TODO: pro kontrolu vytisknu spojeny slovnik
# # print(slovnik_reg_uzivatele)

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

# TODO: pokud je uzivatel registrovany, umozni mu program analyzovat texty
# TODO: importujeme pythonovy soubor 'task_template.py' s texty do aktualniho souboru
from task_template import TEXTS
# TODO: zobrazeni obsahu seznamu
# # print(TEXTS[0])        
# TODO: dame uzivateli vybrat cislo, kterym vybere text pro analyzu
vybrane_cislo_textu = int (input("Zadejte cislo od 1 do 3, vyberete tim text k analyze: "))
print()
# # print("Vybrany text je: ", sep='\n')
# # # # print((TEXTS[int(vybrane_cislo_textu)-1]))
# # print(TEXTS[vybrane_cislo_textu-1])

# 1. možnost #
# #   if ((vybrane_cislo_textu == 1) or (vybrane_cislo_textu == 2) or (vybrane_cislo_textu == 3)):
# 2. možnost #
# # if ((vybrane_cislo_textu >=1) and (vybrane_cislo_textu <=3)):
# #        print("Vybrany text je: ", sep='\n')
# #        # # print((TEXTS[int(vybrane_cislo_textu)-1])) # pou6ijeme int tady pokud nebude dan pred inputem
# #        print(TEXTS[vybrane_cislo_textu-1])
#  TODO: pokud vybere cislo nebo jiny vstup, ktery neni v zadani, program vypíše text a ukonci se
# # else:
# #        print("Zadany text neexistuje!")
# #        quit()

# 3. možnost #
vyber = [1, 2, 3]
def je_hodnota_v_listu(vybrane_cislo_textu, vyber):
       return vybrane_cislo_textu in vyber

if je_hodnota_v_listu(vybrane_cislo_textu, vyber):
       print(f"Zvolili jste text cislo {vybrane_cislo_textu}.")
       print((TEXTS[(vybrane_cislo_textu)-1]), sep='\n')
       
else:
       print("Zadany text neexistuje!")
       quit()
print(55 * oddelovac)
    
# 4. možnost #
# # if (vybrane_cislo_textu == 1):
# #     print(TEXTS[vybrane_cislo_textu-1])
# # elif (vybrane_cislo_textu == 2):
# #     print(TEXTS[vybrane_cislo_textu-1])
# # elif (vybrane_cislo_textu == 3):
# #     print(TEXTS[vybrane_cislo_textu-1])
# # else:
# #     print("Zadany text neexistuj!")
# #     quit()

# TODO: pro vybrany text spocita nasledujici statistiky
    # pocet slov - pracujeme jen s vybranym textem, samostatnymi slovy, vsechna velka pismena prevede na mala
        # rozdeleni textu na slova
jednotliva_slova = []
for slovo in TEXTS[(vybrane_cislo_textu)-1].split():
       ciste_slovo = slovo.strip('.,!<>?:')
       # print(ciste_slovo)
       jednotliva_slova.append(ciste_slovo)

# print(jednotliva_slova)
        # pocet slov
pocet_slov = len(jednotliva_slova)
print()
print(f'Pocet slov v textu je: {pocet_slov}.')
print()
# vyskyt slov v textu
def pocet_vyskytu_slov(text):
       pocet_vyskytu = {}
       for slovo in text:
              if slovo.lower() not in pocet_vyskytu:
                     pocet_vyskytu[slovo.lower()] = 1
              else:
                     #pocet_vyskytu_slov[slovo] = pocet_vyskytu_slov[slovo] + 1
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
              if slovo[0].istitle() == True:
                     pocet_slov_Vp += 1
       return pocet_slov_Vp

# počet slov psaných velkými písmeny
def pocet_slov_velkaP(text):
       pocet_velkaP = 0
       for slovo in text:
              if slovo.isupper() == True:
                     pocet_velkaP += 1
       return pocet_velkaP

# počet slov psaných malými písmeny
def pocet_slov_malaP(text):
       pocet_malaP = 0
       for slovo in text:
              if slovo.islower() == True:
                     pocet_malaP += 1
       return pocet_malaP

# počet čísel (ne cifer)
def pocet_cisel(text):
       pocet = 0
       for slovo in text:
              if slovo.isdigit() == True:
                     pocet += 1
       return pocet

# fce, ktr projde na vstupu nahodny text a vraci list pouze cisla
def cisla(text):
       output = []
       for slovo in text:
              if slovo.isdigit() == True:
                     output.append(slovo)
       return output

# sumu všech čísel (ne cifer) v textu
def suma_cisel(cisla):
       suma = 0
       for cislo in cisla:
              suma += int(cislo)
       return suma

 
# MAIN #
print(f"Pocet vyskytu slov: {pocet_vyskytu_slov(jednotliva_slova)}")
print(f"Pocet slov zacinajicich velkym pismenem je v textu {pocet_slov_zVp(jednotliva_slova)}")
print(f"Pocet slov psanych velkymi pismeny je v textu {pocet_slov_velkaP(jednotliva_slova)}")
print(f"Pocet slov psanych malymi pismeny je v textu {pocet_slov_malaP(jednotliva_slova)}")
print(f"Pocet císel v textu je {pocet_cisel(jednotliva_slova)}")
print(f"Cisla v textu jsou {cisla(jednotliva_slova)}")
print(f"Soucet cisel v textu je {suma_cisel(cisla(jednotliva_slova))}")
print(f"Pet nejcastejsich slov jsou {pet_nej_vyskytu(pocet_vyskytu_slov(jednotliva_slova))}")
slovnik_do_grafu(pet_nej_vyskytu(pocet_vyskytu_slov(jednotliva_slova)))