class bomb:
    def __init__ (self,code,color,time):
        bomb.code=code
        bomb.color=color
        bomb.time=time

i,j,k=input().split()
bomb1=bomb(i,j,k)

print("code :",bomb1.code)
print("color :",bomb1.color)
print("second :",bomb1.time)