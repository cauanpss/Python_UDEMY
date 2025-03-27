#bids_dict = {'Cauan': '126',
#             'Murilo': '189'}  
bids_dict = {}
value = []
winner = ''

while True:
    name = input("What's your name?")
    bid = float(input("What's your bid? $ "))
    follow_up = input("Are there any other's bid? [y/n]").lower()
    bids_dict[name] = bid
    value.append(bid)
    print('\n' * 1000)
    if follow_up == 'n':
        break

value_max = float(max(value))

for pessoa in bids_dict:
    if bids_dict[pessoa] == value_max:
        winner = pessoa

print(f"The winner is {winner}, with a bid of {value_max}")
