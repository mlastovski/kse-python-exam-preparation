def to_cube(input_list):
    cube_list = []
    for i in input_list:
        i = i ** 3
        cube_list.append(i)
    print(cube_list)

to_cube(input_list=[1,2,3,4,5,6,7,8,9])