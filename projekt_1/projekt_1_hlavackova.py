"""
projekt_1_hlavackova.py: prvni projekt do Engeto Online Python Akademie

author: Aneta Flachs (Hlavackova)
email: aneta.hlavackova@skanska.cz
"""
# do pameti zapisi registrovane uzivatele s hesly jako listy, ktere propojim do slovniku:
user = ["bob", "ann", "mike", "liz"]
password = [123, "pass123", "password123", "pass123"]
slovnik_reg_uzivatele = dict(zip(user, password))

# pro kontrolu vytisknu spojeny slovnik
print(slovnik_reg_uzivatele)

