def solution(A):
    maximum_sum = -1

    for i in range(len(A)):
        for j in range(i + 1, len(A)):

            current_value = sum(int(digit) for digit in str(A[i]))
            consecutive_value = sum(int(digit) for digit in str(A[j]))

            if current_value == consecutive_value:
                current_sum = A[i] + A[j]
                maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum


print(solution([51, 17, 71, 42]))

