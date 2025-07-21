num1 = 8
num2 = 4
def calculate (num1, operator, num2):
   if operator == "+":
    return (num1 + num2)
   elif operator == "-":
    return (num1 - num2)
   elif operator == "*" :
    return (num1 * num2)
   elif operator == "/" :
    return (num1/num2)
   else :
     print ("please enter valid operator")
print(calculate (num1,"+",num2))
print(calculate (num1,"-",num2))
print(calculate (num1,"*",num2))
print(calculate (num1,"/",num2))