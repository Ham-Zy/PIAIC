#* ================================================== *#
#* ======= Complex Logical Conditions Example ======= *#
#* ================================================== *#

bobzi_runs = 36
total_balls = 20
total_sixes = 5

a = bobzi_runs >= 50 and total_balls
b = total_balls < bobzi_runs
c = total_sixes >= 5


# 1.    False       and            True           or      True
# 2.               False                          or      True
# 3.                           True
if bobzi_runs >= 50 and total_balls < bobzi_runs or total_sixes >= 5 :
    print("👑 King")

else:
    print("🔔 King")