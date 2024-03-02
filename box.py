def solution(A):
    N = len(A)  # number of boxes
    moves = 0  # initialize the number of moves

    for i in range(N):
        # calculate the difference between the number of bricks and 10
        diff = A[i] - 10

        if diff > 0:
            # if the difference is positive, we need to move bricks
            if i == 0:
                # if the box is the first one, move the excess bricks to the right
                A[i + 1] += diff
            elif i == N - 1:
                # if the box is the last one, move the excess bricks to the left
                A[i - 1] += diff
            else:
                # if the box is in between, move the excess bricks to the left if the box on the left has fewer bricks, otherwise move them to the right
                if A[i - 1] < A[i + 1]:
                    A[i - 1] += diff
                else:
                    A[i + 1] += diff

            # increment the number of moves
            moves += diff
        elif diff < 0:
            # if the difference is negative, it means there are not enough bricks in the box
            return -1

    return moves