# Problem Description
# Akash likes playing with strings. One day he thought of applying following operations on the string in the
# given order:

# 1. Concatenate the string with itself.
# 2. Delete all the uppercase letters.
# 3. Replace each vowel with '#'.
# You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the resultant string
# after applying the above operations.
# NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.

# Problem Constraints
# 1<=N<=100000

# Input Format
# First argument is a string A of size N.

# Output Format
# Return the resultant string.

# Example Input
# Input 1:
# A="aeiOUz"

# Input 2:
# A="AbcaZeoB"

# Example Output
# Output 1:
# "###z###z"

# Output 2:
# "bc###bc###"

# Example Explanation
# Explanatino 1:
# First concatenate the string with itself so string A becomes "aeiOUzaeiOUz".
# Delete all the uppercase letters so string A becomes "aeizaeiz".
# Now replace vowel with '#', A becomes "###z###z".

# Explanatino 2:
# First concatenate the string with itself so string A becomes "AbcaZeoBAbcaZeoB".
# Delete all the uppercase letters so string A becomes "bcaeobcaeo".
# Now replace vowel with '#', A becomes "bc###bc###".


def string_operations(A: str) -> str:
    result = ''

    for i in range(len(A)):
        if 65 <= ord(A[i]) <= 90:
            pass
        elif A[i] in ['a', 'e', 'i', 'o', 'u']:
            result = result + '#'
        else:
            result = result + A[i]

    return result * 2


if __name__ == "__main__":
    a = "aeiOUz"
    print(string_operations(a))
