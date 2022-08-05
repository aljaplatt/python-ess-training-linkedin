import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(random.choice(cards))

def deal_card():
    """ Returns random card from the deck """
    random_card = random.choice(cards)
    print('RANDOM CARD: ', random_card)

    return random_card

def calculate_score(cards):
#? Take in a list of cards and return the score calculated from the cards 
    total = sum(cards)
    if total == 21 and len(cards) == 2:
        return 0
    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
        
    return total

user_cards = []
computer_cards = []

for _ in range(2):
    #* This is the same as doing,
    # new_card = deal_card()
    # user_cards.append(new_card)
    #* This,
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

#* We want to calculate tht user and computer scores after they've been dealt, so we move the calc score function up so we can call it here
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f" Your cards: {user_cards}, current score: {user_score}")
print(f" Computers first card: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
else:
    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_should_deal == 'y':
        user_cards.append(deal_card())
    else: 
        is_game_over = True
