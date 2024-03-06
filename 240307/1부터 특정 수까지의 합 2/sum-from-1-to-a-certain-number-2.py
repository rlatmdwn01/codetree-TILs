N=int(input())

def sum_1_to_N(N):
    if N==1:
        return 1
    return sum_1_to_N(N-1)+N

print(sum_1_to_N(N))