'''get input from user of word
get imput for shift
do it '''
A2Z=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def caesar_cipher():
    print("this is a caesar cipher, to encrypt a word by inputing a positive number as the shift, to decode input a negative")
    print("what is your word?")
    word = input()
    print("what is your shift?")
    shift = int(input())
    word = word.upper()
    new_word = []
    for letter in word:
        if letter in A2Z:
            index = A2Z.index(letter)
            new_index = (index + shift) % 26
            if new_index > 25:
                new_index = new_index - 26
            new_word.append(A2Z[new_index])
        else:
            new_word.append(letter)
    print("your new word is " + ''.join(new_word))
caesar_cipher()