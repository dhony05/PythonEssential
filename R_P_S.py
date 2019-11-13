

rock = ["r","R","rock","Rock","Rock".upper()]
paper = ["p","P","paper","Paper","Paper".upper()]
scissors = ["s","S","scissors","Scissors","Scissors".upper()]
def gameRuler(user1, user2):
    if(user1 == user2 ):
        print("draw")
    elif(user1 in rock and user2 in paper):
        user2 = user2 + 1 
        if(user2_wins <= 1):
            print("User2 have "+ user2_wins + " point." )
        else:
            print("User2 have "+ user2_wins + " points.")

    elif(user2 in rock and user1 in paper):
        user1 = user1 + 1 
        if(user1_wins <= 1):
            print("User1 have "+ user1_wins + " point." )
        else:
            print("User1 have "+ user1_wins + " points.")


user1_wins = 0
user2_wins = 0
turns = 0

    

gameRuler("S","R")




# while turns < 4:
#     user1 = input("Enter : Rock, Paper or Scissors:")
#     user2 = input("Enter : Rock, Paper or Scissors:")

#     # gameRuler(user1,user2)

#     turns  = turns -1

    