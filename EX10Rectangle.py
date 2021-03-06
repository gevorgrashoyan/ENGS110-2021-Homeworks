
def drawWithWhile(N, M):
    print("Printing with While Loop")

    currRow = 0
    while (currRow < M):
        if (currRow == 0 or currRow == (M-1)):
            print(N * "*")
        else:
            currCol = 0
            while (currCol < N):
                if (currCol == 0 or currCol == (N-1)):
                    print("*", end="")
                else:
                    print(" ", end="")

                currCol +=1
            print("")
        currRow +=1


def drawWithFor(W, H):
    print("Printing with For Loop")
    for currRow in range(1, H+1):
        if (currRow == 1 or currRow == H):
            print(W * "*")
        else:
            for currCol in range(1, W+1):
                if (currCol == 1 or currCol == W):
                    print("*", end="")
                else:
                    print(" ", end="")
            print("")
    
def main():
    N = int(input("please insert the width of the rectangle"))
    M = int(input("please insert the height of the rectangle"))
    
    drawWithWhile(N, M)
    drawWithFor(N, M)

main()
