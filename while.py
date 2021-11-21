
def my_func():
    ii = 1 # iteration value number
    A_val = int(input("input A value: "))
    B_val = int(input("input B value: "))
    V_val = int(input("input V value: "))
    while A_val <= B_val:
        if A_val <= B_val:
           print(" iteration number " + str(ii) + " result = " + str(A_val))
           ii = ii + 1
           A_val = A_val + V_val
           if A_val > B_val:
               # print(str(A_val) + " ")
               print(" iteration number " + str(ii) + " result = " + str(A_val))
        else:
            break
my_func()

input()
