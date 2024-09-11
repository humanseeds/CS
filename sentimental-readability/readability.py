from cs50 import get_string

# promt user for text
text = get_string("Input Text: ")

# count the number of letters in the text
num_letters = 0
for letter in text:
    if letter.isalpha():
        num_letters += 1

# count the number of words in the text
num_words = 1
for character in text:
    if character.isspace():
        num_words += 1

# count the number of sentences in the text
num_sentences = 0
for characters in text:
    if character in [".", "!", "?"]:
        num_sentences += 1

# computer the Coleman-Liau index
L = (num_letters / num_words) * 100
S = (num_sentences / num_words) * 100
index = 0.0588 * L - 0.296 * S - 15.8

# Print the grade level
if index < 1:
    print(" Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {round(index)}")
