from cs50 import get_float

# ask user for how much change is owed.
#loop until amount is greater than zero
while True:
   change = get_float("Change Owed: ")
   if change  >= 0:
    break

# convert the amount of change to cents
change = round(change * 100)

#create a list of denominations for quaters, dimes, nickles, pennies
denominations = [25, 10, 5, 1]

#create a coin counter set to zero
coin_count = 0

#itterate over the list of denominations
#increase coin count after each loop
for coin in denominations:
    while change >= coin:
        change -= coin
        coin_count += 1

#print the coin count
print(coin_count)
