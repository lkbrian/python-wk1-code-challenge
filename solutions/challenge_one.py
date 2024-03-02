def solution(Array):
    total_sum = sum(Array)
    length = len(Array)
    target = int(total_sum / length)
    # the target is the value that ensures all elements are equal

    if total_sum % length != 0 or target != 10:
        return f"{-1} - It is not possible to end up with exactly 10 bricks in each box"

    moves = 0
    # variable to track the moves
    for i in range(length - 1):
        difference = Array[i] - target

        if difference < 0:

            moves += abs(difference)
            Array[i] += abs(difference)
            Array[i + 1] -= abs(difference)

        elif difference > 0:

            moves += difference
            Array[i + 1] += difference
            Array[i] -= difference

    return f"The number of moves is {moves} & the resulting array is {Array} "
     


print(solution([7, 14, 10, 9]))
# solution([7, 14, 10])
