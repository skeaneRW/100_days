

def cipher():
    alphabet = ['a','b','c','d','e','f','g','h','i','j',
        'k','l','m','n','o','p','q','r','s',
        't','u','v','w','x','y','z']
    
    def get_inputs():
        def get_action():
            action = input("do you want to decode or encode a message?  ")
            if action.lower() in ['decode', 'encode']:
                return action.lower()
            else: 
                print('please choose a valid option')
                return get_action()
        action = get_action()
        cipher_string = input(f"what's the message that you would like to {action}? ")
        shift_query = int(input("what's the number to shift?  "))
        num_shift = shift_query % len(alphabet)
        print(num_shift)
        return {"action": action, "str": cipher_string, "num_shift": num_shift}

    def get_message (str, action, num_shift):
        beginning_part = (alphabet[0:num_shift])
        ending_part = (alphabet[num_shift:])
        coded_alphabet = ending_part + beginning_part
            
        def decode(str):
            encoded_string_list = list(str)
            for i, char in enumerate(str):
                if char.isalpha():
                    idx = coded_alphabet.index(char.lower())
                    encoded_string_list[i] = alphabet[idx]
            return(''.join(encoded_string_list))

        
        def encode(str):
            string_list = list(str)
            for i, char in enumerate(str):
                if char.isalpha():
                    idx = alphabet.index(char.lower())
                    string_list[i] = coded_alphabet[idx]
            return(''.join(string_list))

        if action == 'decode':
            return decode(str)
        else:
            return encode(str)
        
    cipher_input = get_inputs()
    result = get_message(cipher_input['str'], cipher_input['action'], cipher_input['num_shift'])
    print(f"your secret message {'is' if cipher_input['action'] == 'encode' else 'was'}... \n    {result}")
    play_again = input("would you like to play again (y/n)?  ")
    if play_again == 'y':
        cipher()
    else:
        "thanks for playing!"


print(cipher())