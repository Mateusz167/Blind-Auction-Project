from art import logo
bids = {}

print(logo)
print("Welcome to the secret auction program.")
continue_auction = True
def find_highest_bidder(bids):
    highest_bid = 0
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
    print(highest_bid)
    winner = [key for key, value in bids.items() if value == highest_bid]
    print(f"The winner is {winner} with a bid of ${highest_bid}")

def clear_screen():
    # Simulate clearing the screen by printing a large number of newlines
    print("\n" * 100)

while continue_auction:
    name = input("What is your name: ")
    price = int(input("What is your bid: "))
    bids[name] = price

    decision = input("Are there any other bidders? Type 'yes' or 'no'")
    if decision == 'no':
        continue_auction = False
        find_highest_bidder(bids)
    elif decision == 'yes':
        clear_screen()




