N=int(input())

def print_HelloWorld(N):
    if N==0:
        return
    else:
        print_HelloWorld(N-1)
        print("HelloWorld")

print_HelloWorld(N)