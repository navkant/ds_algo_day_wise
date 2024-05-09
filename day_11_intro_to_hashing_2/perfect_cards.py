# Problem Description
# Tom and Harry are given N numbers, with which they play a game as a team.
# Initially, Tom chooses a particular number P from the N numbers, and he takes away all the numbers that are equal to P.
# Next, Harry chooses a different number Q, different from what Tom chose, and takes away all the numbers equal to Q
# from the remaining N numbers.
# They win the game if they can take all the numbers by doing the above operation once and if each of them has the
# same amount of numbers towards the end.

# If they win, return the string "WIN", else return "LOSE".

# Problem Constraints
# 2 <= N <= 100
# 1 <= A[i] <= 100

# Input Format
# The first and the only argument of input contains an integer array, A.

# Output Format
# Return a string, denoting the answer.

# Example Input
# Input 1:
#  A = [1, 2]

# Input 2:
#  A = [1, 1, 2, 2, 3]

# Example Output
# Output 1:
#  "WIN"

# Output 2:
#  "LOSE"

# Example Explanation
# Explanation 1:
#  In the his turn, Tom can take 1 away, and then Harry take take 2 away. The array is empty and both of them have
#  equal number of cards, so we can say that they have won the game.

# Explanation 2:
#  No matter how they take away the elements, >= 1 card will always remain, hence, they lose.

from typing import List


def solve(A: List[int]):
    hash_map = dict()

    for i in A:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] += 1

    if len(hash_map.keys()) > 2 or len(hash_map.keys()) < 2:
        return "LOSE"
    else:
        for number in hash_map.keys():
            freq = hash_map[number]
            if freq == len(A) / 2:
                return "WIN"
            else:
                return "LOSE"



if __name__ == "__main__":
    a = [1, 100]
    print(solve(a))
