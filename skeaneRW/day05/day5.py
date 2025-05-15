'''
password generator: 
1. ask how many characters the password should be
2. ask how many special characters should be included
3. ask how many numbers should be included
4. generate a password using uppercase letters, lowercase letters, numbers and special characters.
'''
import random

def create_pass():
    print("welcome to the password generator")
    pass_chars = []

    def get_pass_len():
        n = input("how long should your password be?  ")
        if n.isdigit() and int(n) >= 6:
            return(int(n))
        else:
            print("please choose a valid number; passwords should be at least 6 characters long   ")
            return get_pass_len()
    
    pass_len = get_pass_len()

    def get_len(max_chars, char_type):
        char_count = input(f"how many {char_type} should be included? (answer: 0-{max_chars})   ")
        if char_count.isdigit() and int(char_count) <= max_chars:
            return int(char_count)
        else:
            print(f"please choose a number between 0 and {max_chars}   ")
            return get_len(max_chars)
    
    def get_special_chars(max_chars):
        list_size = get_len(max_chars, "special characters")
        possible_special_chars = ['@', '#', '?', '^', '%', '!']
        for _ in range(0, list_size):
            random_char = random.choice(possible_special_chars)
            pass_chars.append(random_char)
        return
    
    def get_numbers(max_chars):
        list_size = get_len(max_chars, "numbers")
        possible_numbers = [0,1,2,3,4,5,6,7,8,9]
        for _ in range(0, list_size):
            random_num = random.choice(possible_numbers)
            pass_chars.append(str(random_num))
        return
    
    def get_letters(max_chars):
        list_size = max_chars
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
                    't', 'u', 'v', 'w', 'x', 'y', 'z']
        for _ in range(0, list_size):
            random_letter = random.choice(alphabet)
            for i in range(0, 2):
                if i == 0:
                    pass_chars.append(random_letter.upper())
                else:
                    pass_chars.append(random_letter.lower())
        return

    get_special_chars(pass_len)
    get_numbers(pass_len - len(pass_chars))
    get_letters(pass_len - len(pass_chars))

    def shuffle_pass(list):
        random.shuffle(list)
        return ''.join(list)
    
    password = shuffle_pass(pass_chars)
    return password


password = create_pass()
print(f"Your generated password is: {password}")

new_password = input("Do you want to generate a new password? (y/n) ").lower()
if new_password == 'y':
    password = create_pass()
    print(f"Your new generated password is: {password}")
elif new_password == 'n':
    print("Thank you for using the password generator! Goodbye!")
else:
    print("I didn't understand that answer. Please enter 'y' or 'n'.")