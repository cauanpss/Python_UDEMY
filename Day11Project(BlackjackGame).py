#Import libraries 
import random, math

#Defining variables
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Defining functions:

#Addicional card
def add_card():
    card_add = random.choice(cards)
    return card_add

#Continuity
def verify_continuity(prompt):
        while True:
            verify= input(prompt).lower()
            if verify not in ('y', 'n'):
                print("ERROR' Pick between 'y', or 'n'.")
            else:
                return verify

#Winning conditions
def check_winner(user_score, pc_score):
    #Checking if exceeded
    if user_score > 21:
        return "You went over! You lose."
    if pc_score > 21:
        return "PC went over.You win!"
    #Comparing scores
    if pc_score > user_score:
        return f"PC score is {pc_score}. And your's {user_score}. You lose." 
    elif user_score > pc_score:
        return f"Your score is {user_score}, and PC scores is {pc_score}. You win!"
    else:
        return "Draw!"
    
def score_calculating(cards):
    '''Calculate score, and if 11 in cards, and score > 21, turn 11 in 1'''
    score = sum(cards)
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score


#Initiating the game loop
while True:
#Starting game
    pc = []
    user = []
    #Providing cards
    for start in range(2):
        pc.append(add_card())
        user.append(add_card())

    #Providing scores
    pc_current_score = score_calculating(pc)
    user_current_score = score_calculating(user)
    
    play_blackjack = verify_continuity('Do you want to play BlackJack?[y/n]:')
    if play_blackjack == 'n':
         break
    print("Ok, let's play!")

#Showing player cards
    print(f"Your cards: {user}, current score: {user_current_score}\n PC first card {pc[0]}")

# Player's turn
    while True:
        another_card = verify_continuity("Type 'y' to pick another card, type 'n' to pass: ")
        if another_card == 'y':
            user.append(add_card())
            user_current_score = score_calculating(user)
            print(f"Your cards: {user}, current score: {user_current_score}\n PC first card {pc[0]}")

#bust        
            if user_current_score > 21:
                print("\nBust! you went over 21!")
                break
        else:
            break

# PC's turns
    if user_current_score <=21:
        while pc_current_score <= 16:
            pc.append(add_card())
            pc_current_score = score_calculating(pc)
    #Adding random plays 
        while 16 < pc_current_score < 18:
            if random.random() < 0.5:
                pc.append(add_card())
                pc_current_score = score_calculating(pc)
        if 18 <= pc_current_score < 21:
            if random.random() < 0.1:
                pc.append(add_card())
                pc_current_score = score_calculating(pc)

        #Check final results
        print("Checking the results:\n ")
        print(f"Your cards: {user}, final score: {user_current_score}\n")
        print(f"PC's cards: {pc}, final score: {pc_current_score}\n")
        print(check_winner(user_current_score,pc_current_score))

    #Another play
    another_play = verify_continuity("Do you want to play again?")
    if another_play == 'y':
        continue
    else:
        break