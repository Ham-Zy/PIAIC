#* ================================================== *#
#* ======== Logical Operators with Variables ======== *#
#* ================================================== *#

bobzi_runs = 36
total_balls = 20
total_sixes = 5


a = bobzi_runs >= 50 and total_balls    # False
b = total_balls < bobzi_runs            # True
c = total_sixes >= 5                    # True


if a and b or c:
    print("👑 King")

else:
    print("🔔 King")