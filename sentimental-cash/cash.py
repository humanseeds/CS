from cs50 import get_float


while True:
   change = get_float("Change Owed: ")
   if change  >= 0:
    break

change = round(change, 2)

