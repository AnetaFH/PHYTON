"""
main.py: prvni projekt do Engeto Online Python Akademie

author: Aneta Flachs (Hlavackova)
email: aneta.hlavackova@skanska.cz
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# MAIN #
# TODO: do pameti zapiseme registrovane uzivatele s hesly jako listy, ktere propojim do slovniku:
user = ["bob", "ann", "mike", "liz"]
password = ["123", "pass123", "password123", "pass123"]
slovnik_reg_uzivatele = dict(zip(user, password))
oddelovac = 42* "-"
moznosti = [1, 2, 3]

# TODO: program si vyzada prihlasovaci udaje uzivatele: jmeno a heslo

uzivatel = input("username:")
heslo = input("password:")

print(oddelovac)
# TODO: zkontroluje, zda je uzivatel registrovany, pokud neni, program se rozlouci a ukonci
if not uzivatel in user:
        print("unregistered user, terminating the program..")
        quit()
elif heslo not in password:
        print("wrong password for user <", uzivatel, ">, terminating the program.. ")
        quit()
else:
       # pokud uzivatel existuje a zadal spravne heslo, umozni mu program analyzovat texty
        print("Welcome to the app, ", uzivatel, "!")
        print("We have 3 texts to be analyzed.")

print(oddelovac)

# TODO: dame uzivateli vybrat cislo, kterym vybere text pro analyzu
vybrane_cislo_textu = int(input("Enter a number btw. 1 and 3 to select: "))
if vybrane_cislo_textu in moznosti:
       print(oddelovac)
else:
       print("Enter text does not exist, terminating the program.. ")
       quit()

# TODO: pro vybrany text spocita nasledujici statistiky
# počet slov
# vygeneruje jednotliva slova z texts, ocisteno o nechtene znaky
jednotliva_slova = []
for slovo in TEXTS[(vybrane_cislo_textu)-1].split():
    ciste_slovo = slovo.strip(".,!<>?:")
    jednotliva_slova.append(ciste_slovo)
pocet_slov = len(jednotliva_slova)
print("There are ", pocet_slov, " words in the selected text.")

# počet slov začínajících velkými písmeny
pocet_slov_VP = 0
for slovo in jednotliva_slova:
       if slovo.istitle():
              pocet_slov_VP += 1
print("There are ", pocet_slov_VP, " titlecase words.")

# počet slov psaných velkými písmeny
pocet_slov_KP = 0
for slovo in jednotliva_slova:
       if slovo.isupper():
              pocet_slov_KP += 1
print("There are ", pocet_slov_KP, " uppercase words.")

# počet slov psaných malými písmeny
pocet_slov_mp = 0
for slovo in jednotliva_slova:
       if slovo.islower():
              pocet_slov_mp += 1
print("There are ", pocet_slov_mp, " lowercase words.")

# počet slov psaných číselnými stringy
pocet_slov_00 = 0
for slovo in jednotliva_slova:
    if slovo.isdigit():
        pocet_slov_00 += 1
print("There are ", pocet_slov_00, " numeric string.")

# suma všech čísel
suma = 0
for cislo in jednotliva_slova:
       if cislo.isdigit():
              suma += int(cislo)
print("The sum of all the numbers ", suma)

print(oddelovac)

# TODO: zobrazime sloupcovy graf prezentujici cetnost ruznych delek slov v textu
    # Hlavička
print(f"{"LEN":<5}| {"OCCURENCES":<12}| {"NR.":<5}")
print(oddelovac)
       
delky = {}
for slovo in jednotliva_slova:
       delka = len(slovo)
       delky[delka] = delky.get(delka, 0) + 1

# Seřadit podle délky a vytisknout graf
for delka in sorted(delky):
       znaky = delky[delka]
       print(f"{delka:>2} | {"*" * znaky} {" "* (20 - znaky)}| {znaky:<20}")