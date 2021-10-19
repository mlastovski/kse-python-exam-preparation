import sys

if int(sys.argv[1]):
    number = int(sys.argv[1])
    result = number * 2
    print(result)
else:
    print('it is not int')