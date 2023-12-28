import sys
def add(num1, num2):
    addition= num1 + num2
    return addition

def sub(num1, num2):
    sub= num1 - num2
    return sub
num1=float(sys.argv[1])
operator=sys.argv[2]
num2=float(sys.argv[3])

if operator == "add":
    output=add(num1, num2)
    print (output)
elif operator == "sub":
    output=sub(num1, num2)
    print(output)
 
# sum=operator(num1, num2)
# sum=add(100,200)
print("Sum of two numbers are: ",output)