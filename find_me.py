import random

B_val = int(input("input interesting you value from 0 to 10: "))

my_list = [0,1,2,3,4,5,6,7,8,9]

ii = 0
while ii <= 9:
    my_list[ii] = random.randint(0, 10)
    ii += 1

print("our list values: " + str(my_list))
print("\n")

def finde_func():
    ii = 0
    while ii <= 9:
        if B_val == my_list[ii]:
            #print("  ")
            print("registred value with number in list " + str(ii))
       # else:
          #  print("may be no value iqual your input in our list")
        ii += 1


finde_func()

input()
