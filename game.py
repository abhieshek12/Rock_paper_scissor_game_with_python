import random 
print (" rock paper scissors")
print(" lets start the game  game  ")
print("""for rock you have to write \"r\" 
for paper you have to write \"p\" 
for scissors you have to write \"s\" """)

print (" your turn first ")

you = input("give your input :").strip()

if not(you.lower() == "r" or you.lower() == "p" or you.lower() == "s" ) :
    print("please give valid input")

dic = { 1 : "rock" , 2 : "paper" , 3 : "scissors" }
anouther_dic = { "r" : "rock" , "p" : "paper" , "s" : "scissors" }

comp = dic[random.randrange(1,4)]
player = anouther_dic[you]

if comp == player :
    print("its a draw ")
    print(f" computer choosed {comp} and you choosed {player}")
elif comp == "rock" :
    if player == "paper" :
        print(f"you won .. computer choosed {comp} and you choosed {player}")    
    else :
        print(f"computer won computer choosed {comp} and you choosed {player}")
elif comp == "paper" :
    if player == "scissors" :
        print(f"you won .. computer choosed {comp} and you choosed {player}")    
    else :
        print(f"computer won computer choosed {comp} and you choosed {player}")
else : # comp = scissors
    if player == "rock" :
        print(f"you won .. computer choosed {comp} and you choosed {player}")    
    else :
        print(f"computer won computer choosed {comp} and you choosed {player}") 
    
                
