import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequences.txt")
        sys.exit(1)


    # TODO: Read database file into a variable
    # create an empty list to store database in
    database = []
    with open(sys.argv[1], "r") as database_file:
        reader = csv.DictReader(database_file)
        for row in reader:
            database.append(row)


    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as sequences_file:
        dna_sequence = sequences_file.read()


    # TODO: Find longest match of each STR in DNA sequence
    # remove the 'name' row from each column and make a dictionary to store each str
    strs = database[0].keys() - {'name'}
    str_count = {}
    # use the helper function to compute matchs for strs in sequences
    for str_sequence in strs:
        str_count[str_sequence] = longest_match(dna_sequence, str_sequence)


    # TODO: Check database for matching profiles
    # loop trough people, if a person is not a match break out and move to next person
    for person in database:
        match = True
        for str_sequence in strs:
            if int(person[str_sequence]) != str_counts[str_sequence]:
                match = False
                break
       #if the person is a match, print their name
        if match:
            print(person['name'])
            sys.exit(0)
    # if no matches found
    print("No match")
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
