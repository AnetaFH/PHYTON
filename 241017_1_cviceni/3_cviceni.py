# user_email = {'email':'marek.parek@gmail.com'}
# print(user_email)
# user_1 = {}
# user_1['name'] = "Marek"
# user_1['surname'] = "Parek"
# user_1.update(user_email)
# print(user_1)


# jmeno = 'Marek'
# heslo = '123'
# uzivatel = {'Marek' : '123'}

# if uzivatel.get(jmeno) == heslo:
#     print('v poradku')
# else:
#     print('ne')


# cisla_1 = (1, 1, 2, 3, 4)
# cisla_2 = (5, 6, 7, 7, 8)
# print(type(cisla_1))

# set_2 = cisla_1 + cisla_2
# print(set_2)
# set_1 = {1}
# print(set_1)
# set_1.update(cisla_1)
# print(set_1)
# sjednocene_sety = set(cisla_1) | set(cisla_2)
# print(sjednocene_sety)

cisla_1 = {1, 2, 3, 4}

cisla_2 = {3, 4, 5, 6}
rozdil_cisel = cisla_1.difference(cisla_2)
print(rozdil_cisel)