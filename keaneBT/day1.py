# band name generator
def start_game():
    city = input('Where are you from? the northeast, the south, the midwest, or the west? ')
    if city == 'northeast':
        part_2 = 'fire'
    elif city == 'south':
        part_2 = 'flamingo'
    elif city == 'midwest':
        part_2 = 'earth'
    elif city == 'west':
        part_2 = 'wind'
    else:
        part_2 = 'unknown'

    print('Cool!')
    pet = input('Do you have a pet? (yes or no) ')
    if pet == 'no':
        Pvalue = 0
        print('Ok')
        print('Your band name is the flaming ' + part_2)
    elif pet == 'yes':
        print('What kind of pet do you have, a dog, a cat, a fish, or something else?')
        pet_type = input()
        if pet_type == 'dog':
            Pvalue = 1
        if pet_type == 'cat':
            Pvalue = 2
        if pet_type == 'fish':
            Pvalue = 3
        if pet_type == 'something eles':
            Pvalue = 4
        if Pvalue == 1:
             print('Your band name is the everyday ' + part_2)
        if Pvalue == 2:
             print('Your band name is the ulitmate '+part_2)
        if Pvalue== 3:
             print ('your band name is the amazing '+part_2)
        if Pvalue == 4:
             print('Your band name is the unknown '+part_2)

start_game()