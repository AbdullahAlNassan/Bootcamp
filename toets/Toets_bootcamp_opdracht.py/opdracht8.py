lijst_eten = ['appel', 'pannekoek', 'kiwi', 'hamburger', 'groentesoep']

print('onze menukaart:')

for gerecht in lijst_eten:
    print(gerecht)

langste_gerecht = max(lijst_eten, key=len)
print(f"Het gerecht met de laatste naam is {langste_gerecht}")