from art import logo
from os import system, name 

def clear():
    # windows 
    if name == 'nt':
        _ = system('cls')
    # mac 
    else:
        _ = system('clear')

print(logo)

bids = {}
#? while loop condition
bidding_finished = False


#? 
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  #? Loop through dict of bidders and bids, 
  for bidder in bidding_record:
    #? bid_amount will give us the value , 123, 321
    bid_amount = bidding_record[bidder]
    #? is bid_amount greater than 0? highest bid becomes 123, then 321 etc 
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      #? if the current bidder has the highest bid, set them to the winner also
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  #? Add name and price to bids dict -L14
  bids[name] = price
  #? Ask if more bidders, wrap this block in while loop. Create loop condition L15
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  

"""
FAQ: My console doesn't clear()

This will happen if you’re using an IDE other than replit. 
I’ll cover how to use PyCharm in Day 15. That said, you can write your own clear() function or configure your IDE like so: 

https://www.udemy.com/course/100-days-of-code/learn/lecture/19279420#questions/16084076

"""