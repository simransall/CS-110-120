
def iterationloop(A, N):
    for i in range(0, N-1):
        print('i = ' + str(i))
        x = i
        print('x=i ' + str(x))
        for j in range(i+1, N):
            print('j = ' + str(j))
            if(A[j] < A[x]):
                x = j
                print('x=j ' + str(x))

def main():
    A = [5,8,9,0,1,2,4]
    N = len(A)
    iterationloop(A, N)

main()
