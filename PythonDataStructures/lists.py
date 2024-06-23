vegan_no_nos = ['eggs', 'cheese', 'meat', 'milk','fish', 'butter']

pie_ingredients = ['flour', 'butter', 'eggs', 'apples','sugar']

for food in pie_ingredients:
    if food in vegan_no_nos:
        print(f"OH NO, CANNOT EAT {food}! IT'S NOT VEGAN!")
    else:
        print(f'YAY, I CAN EAT {food}!')
