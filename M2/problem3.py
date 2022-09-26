a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]

print ("\n")
print ("Type of array before performing the task")
print ( "Type of A1:", type(a1[1]))
print ( "Type of A1:", type(a2[1]))
print ( "Type of A1:", type(a3[1]))
print ( "Type of A1:", type(a4[1]))

def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print (arr)
    print("\nPositive Output:\n")
    
    for i in range(0, len(a4)):
            a4[i] = int (a4[i])

    for num in (arr):
        if num > 0 or num == 0:
            print(num, end = " ")
        else:
            num = num * -1
            print(num, end = " ") 
            
    for i in range(0, len(a4)):
            a4[i] = str (a4[i])                        
print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)

print ("\n")
print ("Type of array after performing the task")
print ( "Type of A1:", type(a1[1]))
print ( "Type of A1:", type(a2[1]))
print ( "Type of A1:", type(a3[1]))
print ( "Type of A1:", type(a4[1]))

