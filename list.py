import random

def my_func():
     B_val = int(input("input Min value in list: "))
     V_val = int(input("input Max value in list: "))

     my_list = [0,1,2,3,4,5,6,7,8,9]

     ii = 0
     while ii <= 9:
       my_list[ii] = random.randint(B_val, V_val)
       ii += 1
     print("  ")
     print("random list values: " + str(my_list))

my_func()

input()
