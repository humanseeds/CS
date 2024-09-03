from cs50 import get_int

# get the height user
while True:
    n = get_int("Height: ")
    if n > 0 and n <= 8:
        break
# create a loop until the height from user
for i in range(n):

    # print the spaces first
    for j in range(n - i - 1):
        print(" ", end="")

    # print the blocks next
    for j in range(i + 1):
        print("#", end="")

    # move to the next line
    print()
