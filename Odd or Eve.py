import random

print("Game starting...\nWelcome to Odd or Eve!")


def select_mode():
    while True:
        mode = input("\nChoose a Mode:\n (1) 1 to 6 \n (2) 1 to 10 \n (3) *CRAZY* \n\n Enter: ")
        if mode == "1":
            return "1 to 6", range(1, 7) 
        elif mode == "2":
            return "1 to 10", range(1, 11) 
        elif mode == "3":
            return "CRAZY",range(1, 11) 
        else:
            print("Invalid choice. Please type 1, 2, or 3.")

def batting(run_range, mode):
    runs = 0
    while True:
        user_bat = int(input(f"\nBatting ({run_range[0]} to {run_range[-1]}): "))
        while user_bat not in run_range:
            print(f"Please enter a number within the range {run_range[0]} to {run_range[-1]}.")
            user_bat = int(input(f"Batting ({run_range[0]} to {run_range[-1]}): "))     
        
        computer_bowl = random.randint(run_range[0],run_range[-1]) 
        
        if mode == "CRAZY":
            if (user_bat == computer_bowl + 1 or user_bat == computer_bowl - 1) or (user_bat == 1 and computer_bowl == 10):
                print(f"OUT! The computer bowled you out! The computer bowled {computer_bowl}.\n\n")
                break
            
            elif computer_bowl == user_bat:
                runs += user_bat ** 2  
                print("Runs Squared!")
                print("Total runs:",runs)
            else:
                runs += user_bat
                print(f"You scored {user_bat}\nTotal runs: {runs}\n")
        else:
            if computer_bowl == user_bat:
                print(f"OUT! The computer bowled you out! The computer bowled {computer_bowl}.\n\n")
                break
            else:
                runs += user_bat
                print(f"You scored {user_bat}\nTotal runs: {runs}\n")

    return runs

def bowling(run_range, mode):

    runs = 0
    while True:
        user_bowl = int(input(f"Bowling ({run_range[0]} to {run_range[-1]}): "))  
        while user_bowl not in run_range:
            print(f"Please enter a number within the range {run_range[0]} to {run_range[-1]}.")
            user_bowl = int(input(f"Bowling ({run_range[0]} to {run_range[-1]}): "))  
        
        computer_bat = random.randrange(run_range[0],run_range[-1])  

        if mode == "CRAZY":
            if (user_bowl == computer_bat + 1 or user_bowl == computer_bat - 1) or (user_bowl == 1 and computer_bat == 10):
                print(f"OUT! You bowled the computer out! The computer batted {computer_bat}.\n\n")
                break
            
            elif computer_bat == user_bowl:
                runs += computer_bat ** 2  
                print("Runs Squared!\n")
            else:
                runs += computer_bat
                print(f"Computer scored {computer_bat}\nTotal runs: {runs}\n")
        else:
            if user_bowl == computer_bat:
                print(f"OUT! You bowled the computer out! The computer batted {computer_bat}.\n\n")
                break
            else:
                runs += computer_bat
                print(f"Computer scored {computer_bat}\nTotal runs: {runs}\n")

    return runs

def play():
    mode, run_range = select_mode() 

    c_toss = random.randint(1, 2)
    print("\n\nTOSS ~~~ Odd or Eve ~~~  \n")
    u_choice = input("Odd or Eve?: ").upper()
    toss_input = int(input("Enter a number for the toss (1 or 2): ")) 
    
    add = c_toss + toss_input  
    toss_result = "EVE" if add % 2 == 0 else "ODD"
    
    
    if toss_result == u_choice:
        print(f"You won the toss!\nResult: {add} ({toss_result})")
        user_decision = input("Do you choose BAT or BOWL? (BAT / BOWL): ").upper()
        
        if user_decision == "BAT":
            user_score = batting(run_range, mode)
            print("\nYOU ARE NOW BOWLING") 
            computer_score = bowling(run_range, mode)  
        else:
            computer_score = bowling(run_range, mode)  
            print("\nYOU ARE NOW BATTING") 
            user_score = batting(run_range, mode)  
    else:
    
        print(f"You lost the toss! Result: {add} ({toss_result}).")
        computer_decision = random.choice(["BAT", "BOWL"]) 
        print(f"The computer chooses to {computer_decision}!\n")
        
        if computer_decision == "BAT":
            computer_score = bowling(run_range, mode)
            print("\n\nYOU ARE NOW BATTING")   
            user_score = batting(run_range, mode)  
        else:
            user_score = batting(run_range, mode)
            print("\n\nYOU ARE NOW BOWLING") 
            computer_score = bowling(run_range, mode) 

    if user_score > computer_score:
        print(f"\nYou win! Your score: {user_score} | Computer's score: {computer_score}")
    elif computer_score > user_score:
        print(f"\nYou lose! Your score: {user_score} | Computer's score: {computer_score}")
    else:
        print(f"\nIt's a tie! Your score: {user_score} | Computer's score: {computer_score} ")
        
    

def play_again():
    while True:
        p = input("\nPlay again? (y/n): ").lower()
        if p == "y":
            play()
            return True
        elif p == 'n':
            print("Exiting...")
            quit()
        else:
            print("Please type in 'y' to play again or 'n' to quit.")
            break

play()
play_again()

