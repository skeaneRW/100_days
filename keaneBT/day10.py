
def get_inputs():
    print("what kind of calulation would you like?")
    cal=input ("+ - / *")
    print (f"evaluating Y {cal} X")
    Y=input ("what is Y?")
    X= input('and X?')
    return cal, X, Y

cal, X, Y=get_inputs()

def cal_inputs(cal, Y, X):
    Y=int(Y)
    X=int(X)
    if cal == '+':
        result= Y + X
    if cal == '-':
        result= Y - X
    if cal == '/':
        result= Y/X
    if cal == '*':
        result= Y*X
    else:
        print ('invalid input try agin')
        return get_inputs()
    result=int(result)
    print (f"{Y}{cal}{X}={result}")
    return result
result=cal_inputs(cal, Y, X)
def play_agnin(result):
    while True:
        print('would you like to contiune')
        tof=input ('y/n').lower()
        if tof=='n':
            print ('thank you')
            return
        if tof=='y':
            Y=result
            cal=input ('+ - / *')
            X=input ('what is X')
            cal_inputs(cal, Y, X)
play_agnin(result)
    #print(result)