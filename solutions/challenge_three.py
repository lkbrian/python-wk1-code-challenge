def solution(N):
    if N < 1 or N > 200000:
        return "Invalid input"

    num_of_letters = min(N, 26)
    letter_count = N // num_of_letters
    remaining = N % num_of_letters

    result = ""
    for i in range(num_of_letters):
        result += chr(ord("a") + i) * letter_count

    for i in range(remaining):
        result += chr(ord("a") + i)

    return result


print(solution(3))
