name = print('wat is jouw naam')
print('naam')
favoriteSeason = input(f'Wat is jouw favorite seizoen "{name}"? A) Lente, B) Zomer, C) Herfst of D) Winter ')
answer = favoriteSeason.lower()

if answer == 'a':
    print("Ik hou ook van de lente!")
elif answer == 'b':
    print("De zomer is voor mij te warm.")
elif answer == 'c':
    print("Mooi he, al die blaadjes die dan van de boom vallen.")
elif answer == 'd':
    print("Is de winter niet erg koud?")
else:
    print("Die ken ik niet...")

import random
favoriteColor = input('En wat is je favoriete kleur? ') 
trueOrFalse = random.randint(0,1)
if trueOrFalse:
    print('Ik vind dat ook een mooie kleur!')
else:
    print('TBH, ik hou niet zo van {}...'.format(favoritecolor))