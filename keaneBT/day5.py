import random
def get_inputs():
    
    pass_len = input("how long should your password be?  ")
    special_chars = input("how many special characters should be included? 0-" + str(pass_len) + "   ")
    captial_let=input ("how many capital letters should be included? 0-" + str(pass_len) + "   ")
    num=input ("how many numbers should be included? 0-" + str(pass_len) + "   ")
    return [pass_len, special_chars, captial_let, num]
pass_inputs=get_inputs() 
def gen_pass(pass_len, special_chars, captial_let, num):
    spec_chars_list=["!","@","#","$","%","^","&","*","?"]
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
                    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
                    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    pos_num=[0,1,2,3,4,5,6,7,8,9]
    sec_pass=[]
    #get list for spec chars
    for a_man_has_fallen_into_the_river_in_lego_city in range (0,int(special_chars)):
    #    print (a_man_has_fallen_into_the_river_in_lego_city)
        sec_pass.append ( random.choice (spec_chars_list))
    for x in range (0,int(captial_let)):
        sec_pass.append (random.choice (alphabet) )
    for y in range (0,int(num)):
        sec_pass.append (random.choice (pos_num))
    print (sec_pass)
    print ("could be your password")
    
gen_pass(pass_inputs[0],pass_inputs[1],pass_inputs[2],pass_inputs[3])