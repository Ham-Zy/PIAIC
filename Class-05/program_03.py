def calculator(num1, num2, operator):
  if operator == '+':
    print(num1 + num2)
  elif operator == '-':
    print(num1 - num2)
  elif operator == '*':
    print(num1 * num2)
  elif operator == '/':
    print(num1 / num2)
  else:
    print("Invalid Operator")

num1 = int(input('Enter your first number'))
operator = input('Enter your operator')
num2 = int(input('Enter your second number'))

calculator(num1,num2 ,operator)




# calculator(2,2,'+')
# calculator(2,2,'*')
# calculator(2,2,'/')