from typing import List

def add_one_to_number(A: List[int]) -> List[int]:
    while A[0] == 0:
        A = A[1:]

    carry_over = 1

    for i in range(len(A)-1, -1, -1):
        result = A[i] + carry_over
        if result > 9:
            carry_over = 1
            A[i] = result % 10
        else:
            A[i] = result
            carry_over = 0

        if i == 0 and carry_over == 1:
            final_array = [carry_over]
            final_array.extend(A)
            A = final_array

        else:
            pass

    return A

if __name__ == "__main__":
    A = [9, 9]
    print(add_one_to_number(A))
