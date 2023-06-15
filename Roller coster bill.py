height = int(input("enter your height"))
age = int(input("enter your age"))
photo = input("do you want a photo? (Y or N)")
bill = 0
if height > 120:
    if age < 12:
        bill = 5
       # print ("you ticket is $5")
    elif age>18:
        bill = 12
       # print ("your ticket is $12")
    else:
        bill = 7
        #print ("your ticket is $7")
    
    if photo == 'y':
        bill = bill+3
    print (f"your final bill is {bill}")
else:
    print ("your too short for the ride")

