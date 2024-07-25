import random
 

while True :
    print ("""
        welcome to rock,paper,scissor \n
        1) Start the game 
        2) exit game
        3) help 
    """)
    Choic = int (input("enter the number  : "))
    if Choic == 1:
      p_point = 0
      c_point = 0
      while True: 
                print("welcome to the rock,paper,scissor")
                players = input (" enter the name : ")
                choose = ["rock","paper","scissor"]
                computer = random.choice(choose)
                print(f"\you choose {players}, computer choose{computer}")

                if players == computer :
                     print(f"two players both {players}, it is tie")
                elif players == "rock":
                     if computer == "scissor":
                          print("break the scissor, you win")
                          p_point+=1
                     else:
                          print("you loss")
                          c_point+=1
                elif players == "paper":
                     if computer == "rock":
                          print("cover the rock, you win") 
                          p_point+=1
                     else:
                          print("you loss")
                          c_point+=1
                elif players == "scissor":
                     if computer == "paper":
                          print("cut the paper , you win ")
                          p_point+=1
                     else:
                          print("you loss")
                          c_point+=1

                print("\n you have "+str(p_point)+"win")
                print("computer has "+str(c_point)+"win")

                if (players == "exit"):
                     break         
    elif Choic == 2:
         print("exited successfully")
    elif Choic == 3:
         print("statement")
    else:
         print("invalid number ")