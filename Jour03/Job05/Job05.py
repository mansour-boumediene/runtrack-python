def calcule(num1,operator,num2):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "/":
        return num1 / num2
    if operator == "*":
        return num1 * num2
    if operator == "%":
        return num1 % num2
    
a=calcule(50, "+", 8)
print(a)
  
