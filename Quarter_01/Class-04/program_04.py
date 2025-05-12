#* ================================================== *#
#* ========= Input Validation with `if-else` ======== *#
#* ================================================== *#

age = input("Enter your age: ")

if age.isdigit():
    num_age = int(age)
    print(f"Valid age: {num_age}")

else:
    print("Enter a valid age")