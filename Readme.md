# set up
   run git clone git@github.com:Monica-mwangi/Toy-problems-week-one-challenge.git
   run pipenv install on your visual studio code terminal
   run pipenv shell to start working on your visual studio

 # Challenge one
# Minimum Number of Moves to Reach 10 Bricks in Each Box

This function, solution(A), takes a list A of N integers as input and returns the minimum number of moves needed to end up with exactly 10 bricks in every box. If this is not possible, the function returns -1.

## Examples

1. For A = [7, 15, 10, 8], the function should return 7. You can perform the following sequence of moves:
   - Move three bricks from box number 1 to the box on the left: [10, 12, 10, 8].
   - Move two bricks from box number 1 to the box on the right: [10, 10, 12, 8].
   - Finally, move two bricks from box number 2 to the last box: [10, 10, 10, 10].

2. For A = [11, 10, 8, 12, 8, 10, 11], the function should return 6. You can perform the following sequence of moves:
   - Move a brick from box number 0 to box number 2 (using two moves).
   - Move a brick from the last box two positions to the left (using two moves).
   - Move a brick from the middle box to each of its neighbors (another two moves).

## Usage

To use this function, pass a list of integers as the argument:

python
A = [7, 15, 10, 8]
minimum_moves = solution(A)
print(minimum_moves)  # Output: 7

# Challenge two
   # Maximum Sum of Numbers with Equal Digit Sum

This function, solution(A), takes an array A consisting of N integers as input and returns the maximum sum of two numbers whose digits add up to an equal sum. If there are no two numbers whose digits have an equal sum, the function returns -1.

## Examples

1. Given A = [51, 71, 17, 42], the function should return 93. There are two pairs of numbers whose digits add up to an equal sum: (51, 42) and (17, 71). The first pair sums up to 93.

2. Given A = [42, 33, 60], the function should return 102. The digits of all numbers in A add up to the same sum, and choosing to add 42 and 60 gives the result 102.

3. Given A = [51, 32, 43], the function should return -1, since all numbers in A have digits that add up to different, unique sums.

## Usage

To use this function, pass an array of integers as the argument:

python
A = [51, 71, 17, 42]
result = solution(A)
print(result)  # Output: 93

# Challenge 3
# Maximum Sum of Numbers with Equal Digit Sum

This function, solution(A), takes an array A consisting of N integers as input and returns the maximum sum of two numbers whose digits add up to an equal sum. If there are no two numbers whose digits have an equal sum, the function returns -1.

## Examples

1. Given A = [51, 71, 17, 42], the function should return 93. There are two pairs of numbers whose digits add up to an equal sum: (51, 42) and (17, 71). The first pair sums up to 93.

2. Given A = [42, 33, 60], the function should return 102. The digits of all numbers in A add up to the same sum, and choosing to add 42 and 60 gives the result 102.

3. Given A = [51, 32, 43], the function should return -1, since all numbers in A have digits that add up to different, unique sums.

## Usage

To use this function, pass an array of integers as the argument:

python
A = [51, 71, 17, 42]
result = solution(A)
print(result)  # Output: 93