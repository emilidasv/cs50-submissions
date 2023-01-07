import csv
import sys


def main():

    # TODO: Check for command-line usage
    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py Database.csv sequences.txt Name")

    dnaDb = []
    # TODO: Read database file into a variable
    filename = sys.argv[1]

    with open(filename) as file:
        # read file to memeory
        csvrec = csv.DictReader(file)
        for rec in csvrec:
            dnaDb.append(rec)
#        print("DnaDB", dnaDb)


    # TODO: Read DNA sequence file into a variable
        with open(sys.argv[2]) as str:
            strstr = str.read()
#            print("sta",strstr)
            #print("dnaDB", dnaDb["name"])






    # TODO: Find longest match of each STR in DNA sequence


            count_AGATC = longest_match(strstr, 'AGATC')
#            print("logatc", count_AGATC)
            count_AATG = longest_match(strstr, 'AATG')
#           print("loaatg", count_AATG)
            count_TATC = longest_match(strstr, 'TATC')
#            print("tatc", count_TATC)
            person = [count_AGATC, count_AATG , count_TATC]
#            print("person", person)

    # TODO: Check database for matching profiles
            found = False
            for strseq in dnaDb:

                substr = [strseq["AGATC"], strseq["AATG"], strseq["TATC"]]
                #print("str[0]",substr )
                if person[0] == int(strseq["AGATC"]) and\
                   person[1] == int(strseq["AATG"]) and\
                   person[2] == int(strseq["TATC"]):

                   found = True
                   name = strseq["name"]
            if found:
                print(name)
            else:
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
