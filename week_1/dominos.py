def board_dominos(M, N):
    if (M <= N and N <= 16):
        total_squares = M * N

        dominos = 2 * 1

        total_dominos_fitting = (total_squares / dominos)

        if (total_squares % dominos == 0):
            return total_dominos_fitting
        else:
            return (total_dominos_fitting - 0.5)

    else:
        print("the number is not accepted")


M, N = map(int, input().split())