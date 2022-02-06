'''
Name: Pat Frohn
Restaurants Program
'''

vegetarian = False
vegan = False
gluten_free = False

vegetarian_response = input('Is anyone in your party a vegetarian? ')
vegan_response = input('Is anyone in your party a vegan? ')
gluten_response = input('Is anyone in your party gluten free? ')

if vegetarian_response == 'yes':
    vegetarian = True


if vegan_response == 'yes':
    vegan = True

if gluten_response == 'yes':
    gluten_free = True

print('Here are your restaurant choices: ')

if not vegetarian and  not vegan and not gluten_free:
    print('Joe\'s Gourmet Burgers')
    

if not vegan and  not gluten_free:
    print('Mama\'s Fine Italian')


if not vegan:
    print('Main Street Pizza')

print('Corner Cafe')
print('Chef\'s Kitchen')
