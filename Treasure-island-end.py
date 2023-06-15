
# import pyfiglet module
import pyfiglet
  
result = pyfiglet.figlet_format("Wellcome to the treasure", font = "3-d" )
print(result)

print (" welcome to Treasure Island. Your mission is to find the treasure")

q1 = input("Which direction you wish to go right or left? \n")
Q1 = q1.lower()

if Q1 == "right":
    print ("Game Over, thanks for joinning")
else:
    print (f"you have choosen to go towards {Q1}")

q2 = input("How do you want to cross the river Swin or wait? \n")
Q2 = q2.lower()

if Q2 == "swin":
    print (f"you have choosen {Q2} and now your dead")
else:
    print (f"Good you have survied by choosing {Q2} and you are now crossing river")

q3 = input("Now there are 3 door infront of you choose wisely between Red , Blue and Yellow")
Q3 = q3.lower()

if Q3 == "Yellow":
    print (f"Congratulation by choosing {Q3} you are the winner")
else:
    print (f"You have made a grave mistake bu choosing {Q3} and now you shell DIE \n ****** GAME OVER ******")