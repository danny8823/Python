# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

go_or_end = 1
name_bid = {}
biggest_bid = 0

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

while go_or_end == 1:
    name = input('What is your name?')
    bid = int(input('What is your bid?: $'))
    name_bid[name] = bid
    print(name_bid)
    more = input('More bidders?: y or n')
    print(more)
    if more == 'y':
        go_or_end = 1
    elif more == 'n':
        for bidder in name_bid:
            if name_bid[bidder] > biggest_bid:
                biggest_bid = name_bid[bidder]

        for name, bids in name_bid.items():
            if bids == biggest_bid:
                print(logo)
                print('biggest bidder is:', name, bids)
                go_or_end = 0
