# ask for age
age = input("How old are you? ")
# 18-21 wristband
if age != "":
    age = int(age)
    if age > 18 and age < 21:
        print("You can enter, but need a wristband")
#21+ drink, normal entry
    elif age >=21:
        print("You can drink and enjoy tge concert")
#too young
    else:
        print("You can't come in little one =( ")
else:
    print("Please enter an age")
