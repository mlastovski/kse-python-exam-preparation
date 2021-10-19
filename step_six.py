import sys

if int(sys.argv[1]):
    n = int(sys.argv[1])
    for i in range(1, n+1):
        result = i ** 2
        print(result)
else:
    print('input is not int')