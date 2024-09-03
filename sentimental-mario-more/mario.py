from cs50 import get_int

# get the height user
while True:
    n = get_int("Height: ")
    if n > 0 and n <= 8:
        break

# create a loop until the height from user
for i in range(n):

    # print the spaces for first pyramid
    for j in range(n - i - 1):
        print(" ", end="")

    # print the blocks for left pyramid
    for j in range(i + 1):
        print("#", end="")

    # print the spaces between the two pyramids
    print("  ", end="")

    # print the right pyramid
    for j in range(i + 1):
        print("#", end="")

    # move to the next line
    print()
