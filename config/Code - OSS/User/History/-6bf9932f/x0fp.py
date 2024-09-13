def findBitonicSublist(A):
 
    if len(A) == 0:
        return
 
    I = [1] * len(A)
 
    for i in range(1, len(A)):
        if A[i - 1] < A[i]:
            I[i] = I[i - 1] + 1

    D = [1] * len(A)
 
    for i in reversed(range(len(A) - 1)):
        if A[i] > A[i + 1]:
            D[i] = D[i + 1] + 1
 
    lbs_len = 1
    beg = end = 0
 
    for i in range(len(A)):
        if lbs_len < I[i] + D[i] - 1:
            lbs_len = (I[i] + D[i] - 1)
            beg = i - I[i] + 1
            end = i + D[i] - 1
 
    print(lbs_len)
    for i in range(beg, end + 1):
        print(A[i], end=" ")
    print()

 
 
if __name__ == '__main__':
 
    l = int(input())
    A = []
    while len(A) < l:
        A = [int(i) for i in input().split()]

    findBitonicSublist(A)