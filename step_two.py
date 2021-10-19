import sys

if int(sys.argv[1]):
    number = int(sys.argv[1])
    
    if number % 2 == 0:
        print('even')
    else:
        print('odd')
    
else:
    print('it is not int')