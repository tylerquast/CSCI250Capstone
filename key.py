def key():
    userIn = ""
    while isinstance(userIn, int) == False:
        try:
            userIn= eval(raw_input('Enter the pattern number to dispay: '))
        except NameError:
            print('enter a number value')
        except SyntaxError:
            print('enter a number value')
            
    return userIn
