def solution(A):
    maximum_sum = -1

    for i in range(len(A)):
        for j in range(i + 1, len(A)):

            curren_value = sum(int(digit) for digit in str(A[i]))
            consecutive_value = sum(int(digit) for digit in str(A[j]))

            if curren_value == consecutive_value:
                current_sum = A[i] + A[j]
                maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum


print(solution([51, 17, 71, 42]))

# maximum_sum tracks sum and if the pairs dont add up to eqaul sums return -1
# looping through the list(variable i)
#looping through each value(variable j) starting point is the consecutive value(i+1)
# i is the current value and j is the value ater the current
# str converts string to iterate through each pair Int then convers them back to numbers
# comparing the values if the have same values like 5+1 And 4+2
# now adding the values together
# find the biggest outcome from the pairs
