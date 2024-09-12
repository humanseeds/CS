import csv
import sys


def main():

    # TODO: Check for command-line usage
#sys module gives access to sys.argv for command line arguments
    if len(sys.argv) != 2:
        print("Use only data.csv and sequence.txt")
        sys.exit(1)

    # TODO: Read database file into a variable
# csv module has reader and dictreader
# open csv file and dna sequence, read into memory
# first row of csv is name, column if str
# open text file f using open(filename)
     with open(sys.argv[1], "r") as database:
        reader = csv.DictReader(database)
        print(reader.fieldnames)

    # TODO: Read DNA sequence file into a variable
# For each str, computer longest consecutive repeats in sequence
# f.read()rows = []
    rows = []
    with open("foo.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    # TODO: Find longest match of each STR in DNA sequence
# for each position in sequence, computer str repititons in that position
#for each position, check substrings until str no longer repeats
#compare str counts against each row in csv file
# len(s) for length of string
# s[i:j] takes string s, returns subtring with characters from ith character to jth(not including)

    # TODO: Check database for matching profiles
# save str counts in date structure
# for each row,check if each str count matches. if so, print persons name
# int(x) turns string x into an int
# check every column other than first column(name column)
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
