year = int(input("Enter a year you want to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("it's a leap year")
        else:
            print ("not a leap year")
    else:
        print ("not a leap year")
else:
    print ("not a leap year")
