# There are 100 doors, all closed. In a nearby cage are 100 monkeys.
#
# The first monkey is let out and runs along the doors opening every one. The second monkey is then let out and runs along the doors closing the 2nd, 4th, 6th,… - all the even-numbered doors. The third monkey is let out. He attends only to the 3rd, 6th, 9th,… doors (every third door, in other words), closing any that is open and opening any that is closed, and so on. After all 100 monkeys have done their work in this way, what state are the doors in after the last pass?
#
# Answer with the number of open doors.
#
# Answer is an integer. Just put the number without any decimal places if it's an integer. If the answer is Infinity, output Infinity.
#
# Feel free to get in touch with us if you have any questions

from math import sqrt


def is_prime(number: int) -> bool:
    if number == 1:
        raise ValueError
    if number == 2:
        return True

    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            return False

    return True


def is_perfect_square(number: int) -> bool:

    for i in range(number // 2):
        if i * i == number:
            return True

    return False


def solve():
    count = 0
    for i in range(1, 101):
        if is_perfect_square(i):
            
            count += 1

    return count


if __name__ == "__main__":
    print(solve())
