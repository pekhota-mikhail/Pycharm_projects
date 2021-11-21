#import random

B_val = str(input("input value example 321 : "))

ii_len = len(B_val)

#print("len = " + str(ii_len))
result_value = 0
#print(B_val[1])

ii = 0
while ii <= (ii_len - 1):
       result_value = result_value + int(B_val[ii])
       ii += 1

print("result value = " + str(result_value))

input()
 
