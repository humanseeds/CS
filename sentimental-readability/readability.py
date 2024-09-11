from cs50 import get_string

# promt user for text
text = get_string("Input Text: ")

# count the number of letters in the text
num_letters = 0
for letters in text:
    if isalpha():
    num_letters += 1

# count the number of words in the text
num_words = 1
for words in text:
    if isspace():
    num_words += 1

# count the number of sentences in the text
num_sentences = 0
for sentences in text:
    if text ="." or "!" or "?"
    centences += 1

# computer the Coleman-Liau index
float_L = num_letters / num_words * 100
float_S = Num_sentences / Num_words * 100
index = (0.0588 * float(L) - 0.296 * float(s))

# Print the grade level
if index < 1
    print(" Before Grade 1")
    elif index >= 16
    print("Grade 16+")
else: print("Grade ")
