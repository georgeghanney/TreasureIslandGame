print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇
Cross_road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right':\n").lower()
if Cross_road == "left":
  lake = input("You came to a lake.There is an island in the middle of the lake.\n Type 'wait' to wait for a boat.Type 'swim' to swim across: \n").lower()
  if lake == "wait":
    door = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. \n Which color do you choose? \n").lower()
    if door =="red":
      print("You got burned by fire. Game over.")
    elif door == "yellow":
      print("You have successfully found the treasure,Congratulations!!")
    elif door == "blue":
      print("You entered a room full of beasts. Game over.")
    else:
      print("GAME OVER!!!")
  else:
    print("You got attacked by a hungry trout. Game over.")    
else:
  print("You fell into a hole.Game over!!!")

