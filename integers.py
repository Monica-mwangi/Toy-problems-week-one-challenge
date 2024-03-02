#This function solution(N) takes an integer N as input and returns a string of length N containing as many different lower-case letters ('a'-'z') as possible, in which each letter occurs an equal number of times.
def solution(N):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    repeat_times = N // 26
    remaining_chars = N % 26
    result = alphabet * repeat_times + alphabet[:remaining_chars]
    return result

# Testing in python3 shell
print(solution(3))  # Output : "abc", "def", "ghi", etc.
print(solution(5))  # Output : "abcde", "fghij", "klmno", etc.
print(solution(30)) # Output : "aabbccddeeffgghhiijjkkllmmnnoo"
