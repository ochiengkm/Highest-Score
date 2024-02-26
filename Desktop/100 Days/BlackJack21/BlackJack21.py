#Project BlackJack 21 capstone
import random
cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    new_card=random.choice(cards)
    return new_card
def play_game():
    comp_cards=[]
    user_cards=[]
    game_continue=True
    for _ in range (2):
        comp_cards.append(deal_card())
        user_cards.append(deal_card())
    def calculate_score(cards):    
        if sum(cards)==21 and len(cards)==2:
            return 0
        if sum(cards)>21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
    def compare_score(comp_score, user_score):
        if user_score==comp_score:
            return "Draw! It's a push!"
        elif comp_score==0:
            return "You lose! Computer wins with a Blackjack!"
        elif user_score==0:
            return "You win with a Blackjack!"
        elif user_score>21:
            return "You lose! Your score exceeded 21 and it's a bust!"
        elif comp_score>21:
            return "You win! Computer was busted"
        elif user_score>comp_score:
            return "You win! You got the higher score!"
        else:
            return "You lose!"
    while game_continue:    
        comp_score=calculate_score(comp_cards)
        user_score=calculate_score(user_cards)           
        print(f"Computer first card is {comp_cards[0]}")
        print(f"Your cards are {user_cards} and your current score is: {user_score}")
        if comp_score==0 or user_score==0 or user_score>21:
            game_coninue=False
        else:
            if input("Do you want another card? Type 'y' or 'n': ")== "y":
                user_cards.append(deal_card())
            else:
                game_continue=False
    while comp_score!=0 and comp_score<17:
        comp_cards.append(deal_card())
        comp_score=calculate_score(comp_cards)
    print(f"Your final hand is {user_cards} and total score is: {user_score}")
    print(f"Computer's final hand is {comp_cards} and their total score: {comp_score}")
    print(compare_score(comp_score, user_score))
while input("Do you want to play BlackJack21 Game? Type 'y' or 'n': ")=="y":
    play_game()