from cs50 import get_int


# Prompt for user for a credit card number
while True:
    card_number = int(input("please input credit card number: "))
    if card_number > 0:
        break
    print("invalid credit card number, please try again.")

#initialize variables to be used in the program to 0
working_card = card_number
even_position_sum = 0
odd_position_sum = 0
position = 0

# determine the checksum
while working_card > 0:
    digit = working_card % 10 # % 10 removes last digit
    working_card //= 10  # //10 to move to next digit

   # %2 determines if digit is even (0) or odd (1)
    if position % 2 == 0:
      even_position_sum += digit  #even digits are summed

   #odd digits are doubled and then summed
    else:
        doubled_digit = digit *2
        if doubled_digit > 9:
            #subtract 9 to find the sum of the 2 digits b
            odd_position_sum += doubled_digit - 9
        else :
            odd_position_sum += doubled_digit
    position += 1

#find the checksum by adding the product of the even and odd positions
checksum = odd_position_sum + even_position_sum

# if the checksum doesnt end in 0 the card is invalid
if checksum % 10 != 0:
   print("Invalid")

# determine the card length of the valid card number
else:
    length = 0
    temporary = card_number
    while temporary > 0:
         temporary //= 10 # again %10 removes each digit
         length += 1   #counter increments

    #determine the first 2 digits of the credit card
    starting_digits = card_number
    while starting_digits >= 100:
         starting_digits //= 10

   # sort out which company the credit card number belongs to
    if length == 15 and (starting_digits == 34 or starting_digits == 37):
         print("AMEX")
    elif length == 16 and (starting_digits >= 51 and starting_digits <= 55):
         print("MASTERCARD")
    elif (length == 13 or length == 16) and (starting_digits // 10 == 4):
         print("VISA")
    else:
         print("INVALID")




