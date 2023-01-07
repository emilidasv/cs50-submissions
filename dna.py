import csv
import sys
import itertools


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
        keys = dict.keys(dnaDb[0])
        numberof_keys = len(keys)
#        print(keys)
#        print(numberof_keys)
#        print(keys)

    # TODO: Read DNA sequence file into a variable
        with open(sys.argv[2]) as str:
            strstr = str.read()
#            print("sta",strstr)
            # print("dnaDB", dnaDb["name"])

    # TODO: Find longest match of each STR in DNA sequence
            count_AGATC = longest_match(strstr, 'AGATC')
#            print("logatc", count_AGATC)
            count_AATG = longest_match(strstr, 'AATG')
#           print("loaatg", count_AATG)
            count_TATC = longest_match(strstr, 'TATC')
#            print("tatc", count_TATC)
#            person = [count_AGATC, count_AATG , count_TATC]
#           print("person", person)
            person_count = []
            count = 0
            for tmpkey in keys:
                # person
                count = longest_match(strstr, tmpkey)
                person_count.append((count))
#            print(person_count)
            person = dict(zip(keys, person_count))
            # without first key
            person_sub = dict(itertools.islice(person.items(), 1, len(person)))
#            print("person", person)

    # TODO: Check database for matching profiles
            found = False

            for strseq in dnaDb:

                # str_count = len(strseq)
                # print(len(person_sub))
                # print(len(person))

                # print(len(strseq))

                strseq_sub = dict(itertools.islice(strseq.items(), 1, len(strseq)))
                # print(len(strseq_sub))

                if person_sub == strseq_sub:
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
    return str(longest_run)


main()
