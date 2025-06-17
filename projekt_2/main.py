"""
main.py: druhy projekt do Engeto Online Python Akademie

author: Aneta Flachs (Hlavackova)
email: aneta.hlavackova@skanska.cz
"""

import random

oddelovac = 58 * "-" 

print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(oddelovac)
print("Enter a number:")
print(oddelovac)

# První číslice: náhodně z 1–9 (nesmí být 0)
prvni_cislice = random.choice('123456789')

# Zbývající číslice: náhodně z 0–9, ale nesmí se opakovat
# Vytvoření moznosti_cislic a vyřazení použité číslice
moznosti_cislic = set('0123456789') - set(prvni_cislice)

# Třetí unikátní číslice
zbytek_cislic = random.sample(list(moznosti_cislic), 3)

# Složení ve 4-místné číslo a převedení na list -> později budeme hledat/porovnávat hodnoty na pozicích listu
nahodne_cislo = prvni_cislice + "".join(zbytek_cislic)
hledane_cislo = list(nahodne_cislo)

# hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky,
# FUNKCE:
# fce upozorneni
def upozorneni(cislo):
    if not cislo.isdigit():
        print("Input has to be a number!")
    elif int(cislo) > 9999 or int(cislo) < 1000:
        print("Number is inthe range 1000-9999.")
    elif len(set(cislo)) != len(cislo):
        print("Each cifer must be different!")
    else:
        return True

bulls = 0
cows = 0
kolo = 0
pozice = list(range(4))


# MAIN SKRIPT
# herní kolo
while bulls != 4:
    bulls = 0
    cows = 0
    zk_cislo = input(">>> ")
    kontrola = upozorneni(zk_cislo)
    if kontrola is True:
    # převedeme hádané číslo na list (abychom hodnoty mohli porovnávat mezi listy)
        hadane_cislo = list(zk_cislo)
        
        for i in pozice:
            if hadane_cislo[i] == hledane_cislo[i]:
                bulls += 1
            elif hadane_cislo[i] in hledane_cislo:
                cows +=1
        
        text_b = "bull" if bulls == 1 else "bulls"
        text_c = "cow" if cows == 1 else "cows"
     
        if bulls != 4:
            print(f"{bulls} {text_b}, {cows} {text_c}")
        kolo += 1


    
print(oddelovac)
print("Correct, you've guessed the right number in, ", kolo, " guesses!")
print(oddelovac)
print("That's amazing!")


