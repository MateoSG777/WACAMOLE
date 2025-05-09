def main():

    m=[[0 for i in range (3)] for j in range (5)]
    x = 1
    j = 0
    for k in range (5):
        for i in range (3):
            m [i][j] = x
            x = x + 1
    if j <= 3:
        j = j + 2
    else:
        j = j -1
        if j == 3:
            j = 1
    print(m)
main()