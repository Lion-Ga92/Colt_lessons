for item in range (1, 21):
    if item % 2 == 0 and not item == 4:
        print(str(item) + " is even")
    elif item == 4:
        print("4 is unlucky")
    elif item == 13:
        print("13 is unlucky")
    else:
        print(str(item) + " is odd")
