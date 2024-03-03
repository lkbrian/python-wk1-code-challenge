# python-wk1-code-challenge

I have my files in the Solutions folder each challenge per file

### Challenge one

The solution was to have an equal amount of bricks in all boxes

- The `target` variable ensures that all boxes have an eqaul amount of bricks which is 10 and returns negative one(-1) when not possible.
- `moves = 0` will track the minimum amount of moves.
- `for i in range(length - 1):` Loops through the boxes and find the difference (`difference = Array[i] - target` )that's if the box has many or less bricks in relation to the target
- `if difference < 0:` or `if difference > 0:` Moves are incremented based on the difference and remove the negative value using the absolute method when the difference is less or a negative number based on the current value & the target (`moves += abs(difference)` or `moves += difference`)
- `Array[i] += abs(difference),
          Array[i + 1] -= abs(difference)`Increment the current value of the array then subract from the subsequent value and vice versa

### Challenge Two

The solution was to have the maximum value for paired numbers with an equal sum given a list [51,17,71,42] (like 51 and 42 each pair adds upto 6, 17 and 71 and upto 8 each)

- Using the `maximum_sum` variable we track the maximum sum for values that have an equal sum btn their digits if not posible return -1
- Loop through the array, the first loop with variable`i` is for the first value in the array and `j` for the consecutive value
- The `current_value` variable does the sum for the pair, first convert the value to a string, loop through it and then convert the individual values to integers before doing the sum same for the `consecutive_value` variable
- we then check if the pairs have a match and find their sum, following which we determine which is the bigger sum is the `max()` method
- which is assigned to maximum value as our return value

### Challenge three

The solution is to returns a string of length N containing as many different lower-case letters ('a'-'z') as possible, in which each letter occurs an equal number of times.

- Check if the value passed exceeds the limit provided
- `num_of_letters` number of letters is either what has been passed in or the maximum which is 26
- `letter_count` calculates the number of times each letter wil be repeated
- `remaining` does calculate the remaining character after evenly distributing
- `result` initialized to an empty string is the variable that stores the final output ,
- `for i in range(num_of_letters)` This line starts a loop that iterates over the range of num_of_letters. In each iteration, it performs the following steps:
- - `result += chr(ord('a') + i) * letter_count:` This line generates a lowercase letter based on the index `i`, repeats it letter_count times, and appends the resulting string to the result string.
- `for i in range(remaining):` This line starts another loop that iterates over the range of `remaining`. In each iteration, it performs the following steps:

- - `result += chr(ord('a') + i):` This line generates a lowercase letter based on the index i and appends it to the result string. This loop handles any remaining characters that were not evenly distributed in the first loop.
