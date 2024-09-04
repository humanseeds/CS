from cs50 import get_float

# ask user for how much change is owed.
#loop until amount is greater than zero
while True:
   change = get_float("Change Owed: ")
   if change  >= 0:
    break

# round the amount of change to 0.00 to avoid floating error
change = round(change, 2)

#create a list of denominations for quaters, dimes, nickles, pennies
coins = [25, 10, 5, 1]

#create a coin counter set to zero
coin_count = 0

#itterate over the list of denominations
#increase coin coun after each loop
for coin in coins:
    while change >= coin:
    change -= coin
    coin_count += 1

#print the coin count
print(coin_count)
