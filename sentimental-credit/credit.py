from cs50 import get_int


# Prompt for user for a credit card number
while True:
    card_number = int(input("please input credit card number: "))
    if card_number > 0:
        break
    print("invalid credit card number, please try again.")

#initialize variables to be used in the program to 0
working_cnn = get_int
even_positions = 0
odd_positions = 0

# determine the checksum
while working_card > 0:
    digit = working_card % 10 # % 10 removes last digit
    working_card //= 10  # //10 to move to next digit

   # %2 determines if digit is even or odd
    if position % 2 == 0:
      even_position += digit
    else:
        doubled_digit = digit *2
        if doubled_digit > 9:
            odd_position_sum += doubled_digit - 9
         else : odd_position_sum += doubled_digit
    position+= 1


# sum those digits


# add to remaining digits


# validate checksum


# validate company's number


# validate number's length
