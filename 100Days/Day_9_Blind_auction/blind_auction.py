from replit import clear
from art import logo


print(logo)
print("Welcome to secret auction program")

contestants = []

auction_in_progress=True

def who_won():
  highest_bid=0.0
  winner=0
  for i in range(0,len(contestants)):
    if contestants[i]["bid"]>highest_bid:
      winner=i
      highest_bid=contestants[i]["bid"]

  winner_name = contestants[winner]["name"]
  his_bid=contestants[winner]["bid"]
  print(f"The winner is { winner_name } with a bid of $ {his_bid}")
    

while auction_in_progress:
  contestant_name=input("What is your name?: ")
  bid_value=float(input("What is your bid?: $"))
  contestants.append(
    {
    "name": contestant_name,
    "bid": bid_value,
    }
  )
  more_bidders=input("Are there other bidders? Type 'yes' or 'no'")
  if more_bidders=="no":
    auction_in_progress=False
  clear()
  print(contestants[0]["bid"])

who_won()