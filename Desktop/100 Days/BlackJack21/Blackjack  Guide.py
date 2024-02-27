#Blackjack 21 Capstone Project
import random
cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    card=random.choice(cards)
    return card

def play_game():
    comp_cards=[]
    user_cards=[]

    game_over=False
    for _ in range(2):
        comp_cards.append(deal_card())
        user_cards.append(deal_card())
    
    def calculate_score(cards):
        if sum(cards)==21 and len(cards)==2:
            return 0
        if sum(cards)>21 and 11 in cards:
            cards.remove(11)
            cards.append(1)    
        return sum(cards)

    def compare(user_score, comp_score):
        if comp_score == user_score:
            return "Draw! It's a push."
        elif comp_score==0:
            return "You lose! Computer wins by a blackjacK!"
        elif user_score==0:
            return "You win with a balackjack!"
        elif user_score>21:
            return "You lose! It's a bust!"
        elif comp_score>21:
            return "You win! Computer bust!"
        elif user_score>comp_score:
            return "You win!"
        else:
            return "You lose!"
    
    while not game_over:
        comp_score=calculate_score(comp_cards)
        user_score=calculate_score(user_cards)
        print(f"Your cards are:{user_cards}, current score:{user_score}")
        print(f"Computer first card is:{comp_cards[0]}")
        if comp_score==0 or user_score==0 or user_score>20:
            game_over=True
        else:
            user_deal_again=input("Do you want another card? Type 'y' or 'n': ")
            if user_deal_again=="y":
                user_cards.append(deal_card())
            else:
                game_over=True
    while comp_score!=0 and comp_score<17:
        comp_cards.append(deal_card())
        comp_score=calculate_score(comp_cards)
    print(f"Your final hand is:{user_cards} and your total score is:{user_score}")
    print(f"Computer final hand is:{comp_cards} and total score is:{comp_score}")
    print(compare(user_score, comp_score))
while input("Do you want to play BlackJack 21? Type 'y' or 'n': ")=="y":
    play_game()
##################################################
    
