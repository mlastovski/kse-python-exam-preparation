def return_str_from_list(num_list):
    new_list = [str(x) for x in num_list]
    output = ''.join(new_list)
    print(output)

return_str_from_list(num_list=[1,2,3,4,5,6,777,888,9999,1020])
