print("Wellcome to love calculator")

name1 = input("Please enter your name: \n")
name2 = input("Please enter your name: \n")

combine_name = name1 + name2

lowercase_name_combine_name = combine_name.lower()

#T R U E

t = lowercase_name_combine_name.count('t')
r = lowercase_name_combine_name.count('r')
u = lowercase_name_combine_name.count('u')
e = lowercase_name_combine_name.count('e')

true = t + r + u + e

# L O V E

l = lowercase_name_combine_name.count('l')
o = lowercase_name_combine_name.count('o')
v = lowercase_name_combine_name.count('v')
e = lowercase_name_combine_name.count('e')

love = l + o + v + e

love_score = str(true) + str(love)

#print (f"Your love Score is {love_score}")

if int(love_score) > 90 or int(love_score) < 10:
    print (f"your score is {love_score}, you go together like coke and mentos")   
elif int(love_score) > 40 and int(love_score) < 50:
    print (f"Your score is {love_score}, you are alright together")
else:
    print (f"Your score is {love_score}")