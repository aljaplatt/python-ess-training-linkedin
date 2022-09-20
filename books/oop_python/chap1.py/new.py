#  HigherOrLower

import random

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop() # pops one off the top of the deck and returns it
    return thisCard
    
# Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut

#  Main code
print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

#? The program starts by creating a deck as a list
startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict)
        print(startingDeckList)
score = 50

# print(startingDeckList)

while True:  # play multiple games
    print()
    gameDeckList = shuffle(startingDeckList)
    #?Each card is a dictionary made up of a rank, a suit, and a value. For each round of the game, retrieve the first card from the deck and save the components in variables 
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']    
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()

    #? For the next seven cards, the user is asked to predict whether the next card will be higher or lower than the most recently showing card 
    for cardNumber in range(0, NCARDS):   # play one game of this many cards
        answer = input('Will the next card be higher or lower than the ' + 
                               currentCardRank + ' of ' + 
                               currentCardSuit + '?  (enter h or l): ')
        answer = answer.casefold()  # force lower case
        #? The next card is retrieved from the deck, and its components are saved in a second set of variables 
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

        #? The game compares the user’s answer to the card drawn and gives the user feedback and points based on the outcome 
        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score - 15          

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('You got it right, it was lower')

            else:
                score = score - 15
                print('Sorry, it was not lower')

        print('Your score is:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
        currentCardSuit = nextCardSuit

    #? When the user has made predictions for all seven cards in the selection, we ask if they want to play again 
    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break

print('OK bye')