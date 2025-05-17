def _int_():
    print("what kind of calulation would you like?")
    cal=input ("+ - / *")
    print ('evaluating a'+int(cal),"b")
    A=input ("what is a?")
    B= input('and b?')
    A=int(A)
    B=int(B)
    if cal == '+':
        result= A + B
    if cal == '-':
        result= A - B
    if cal == '/':
        result= A/B
    if cal == '*':
        result=A*B
    print ("your answer is"+ int(result))
_int_()