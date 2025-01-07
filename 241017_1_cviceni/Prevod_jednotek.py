# prevodni pomery k jednotkam
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

# Dále vytvoř proměnné s počtem jednotek kg_pocet , km_pocet, l_pocet:
kg_pocet = 80
km_pocet = 54
l_pocet = 5

# promenne prevodu
lb_vysledek = kg_pocet * kg_lb
mile_vysledek = km_pocet * km_mile
gal_vysledek = l_pocet * l_gal

# Vypis vysledku
print (kg_pocet,' kg je ' ,lb_vysledek, 'lb'  )
print (km_pocet, ' km je ', mile_vysledek, 'mil')
print (l_pocet, 'l je ', gal_vysledek, 'gal' )