age = input("Enter your age: ")
number_age = int(age)

if number_age >= 18:
  print("You are allowed")
  print("welcome")
else:
  print("You are not allowed")


# Logical Operators
# AND  agr saray conditions true han to true ay ga
# OR   agr ak bhi condition true ha to true ay ga
age = 10
name = "Hamza"
logical_and = age > 18 and name == "Hamza"
#               True and True

logical_or = age > 18 or name == "Hamza"
print(logical_or)


percentage = int(input("Enter your percentage: "))
if percentage >= 90 and percentage <= 100:
  print("A1 Grade")
elif percentage >= 80:
  print("A Grade")
elif percentage >= 70:
  print("B Grade")
else:
  print("You are fail")
