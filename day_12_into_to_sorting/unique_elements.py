# You are given an array A of N elements. You have to make all elements unique. To do so, in one step you can
# increase any number by one.
# Find the minimum number of steps.

# Problem Constraints
# 1 <= N <= 105
# 1 <= A[i] <= 109

# Input Format
# The only argument given is an Array A, having N integers.

# Output Format
# Return the minimum number of steps required to make all elements unique.

# Example Input
# Input 1:
#  A = [1, 1, 3]

# Input 2:
#  A = [2, 4, 5]

# Example Output
# Output 1:
#  1

# Output 2:
#  0

# Example Explanation
# Explanation 1:
#  We can increase the value of 1st element by 1 in 1 step and will get all unique elements. i.e [2, 1, 3].

# Explanation 2:
#  All elements are distinct.

from typing import List


def unique_elements(A: List[int]):
        hash_map = dict()
        A = sorted(A)
        for i in range(len(A)):
            if A[i] not in hash_map:
                hash_map[A[i]] = 1
            else:
                hash_map[A[i]] += 1
        print(A)
        print(hash_map)
        count = 0

        for i in range(len(A)):
            element = A[i]

            while hash_map[A[i]] > 1:
                if element not in hash_map:
                    hash_map[element] = 1
                    hash_map[A[i]] -= 1
                    A[i] = element
                else:
                    element += 1
                    count += 1

        return count


if __name__ == "__main__":
    A = [2, 2, 3, 5, 17, 18, 17, 2, 19, 20]
    print("input")
    print(A)
    print(unique_elements(A))