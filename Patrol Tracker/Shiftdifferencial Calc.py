print("Hello! Welcome to the MGH patrol tracker!")
print("This tracker will tell you how many patrols you need to do and how much you'll make on the shift!")
name=input("Whats your name? ")
pos=input("Whats your position? ")
print("Welcome " + pos +" " + name + " lets get to work!")

PayRate= int(input("How much do you get paid? "))

ShiftType=input("What shift are you working today? Day, Evening, Night? ")

WeekendShift=input("Is it a weekend shift?(Y/N) ")

if WeekendShift == "Y":
    WeekendShift = True
elif WeekendShift == "N":
    WeekendShift = False

ShiftLength= int(input("How long is the shift your working today? (8 or 12) "))

if ShiftLength <= 8:
    print("You have two sets of patrols for your shift!")
    
if ShiftLength >= 12:
    print("You have three sets of patrols for your shift!")
    
#Pay Calculator
BasePay= PayRate * ShiftLength
print("BasePay: $" + str(BasePay))

EveDiff=.88
NightDiff=1.12
WeekendDiff=1.10

# Calculate pay difference based on shift type
if ShiftType == "Evening":
    PayDiff = BasePay * EveDiff
elif ShiftType == "Night":
    PayDiff = BasePay * NightDiff
else:
    PayDiff = BasePay  # If it's a day shift, no shift differential
    
print("\n")
print("Pay for your shift type: $" + str(PayDiff))
    
# Apply weekend shift multiplier if it's a weekend
if WeekendShift:
    PayDiff *= WeekendDiff
    print("Weekend shift pay: $" + str(PayDiff))