#* ================================================== *#
#* ========= Removing Elements with `pop()` ========= *#
#* ================================================== *#

# #                0           1        2        3
items = [ "Hara dhaniya", "Podina", "Dahi", "Andey" ]

print(items)
items.pop() # remove "Andey"          # items = [ "Hara dhaniya", "Podina", "Dahi" ]
items.pop() # remove "Dahi"           # items = [ "Hara dhaniya", "Podina" ]
items.pop() # remove "Hara dhaniya"   # items = [ "Hara dhaniya" ]
print(items)