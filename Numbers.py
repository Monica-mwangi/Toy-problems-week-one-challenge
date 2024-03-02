#calculates the sum of the digits of a number
def digit_sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

#Iterate over the numbers in the array A and compare each pair of numbers to find the maximum sum
def solution(A):
    max_sum = -1
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if digit_sum(A[i]) == digit_sum(A[j]):
                pair_sum = A[i] + A[j]
                max_sum = max(max_sum, pair_sum)
    return max_sum

A = [51, 71, 17, 42]
result = solution(A)
print(result)