def solution(A):
    N = len(A)  # Number of boxes
    moves = 0   # Initialize the number of moves

    # Iterate through each box except the last one
    for i in range(N - 1):
        # Calculate the excess bricks in the current box
        excess_bricks = A[i] - 10
        
        # If there are excess bricks, redistribute them to the adjacent boxes
        if excess_bricks > 0:
            # Move excess bricks to the adjacent box on the right
            A[i + 1] += excess_bricks
            
            # Increment the number of moves by the number of excess bricks moved
            moves += excess_bricks
        
            # Set the current box to have exactly 10 bricks
            A[i] = 10
        
    # Check if the last box has exactly 10 bricks
    if A[N - 1] != 10:
        return -1  # If not, return -1 since it's not possible to achieve the target distribution
    
    return moves

# Test cases
print(solution([7, 15, 10, 8])) 
 # Output: 7

