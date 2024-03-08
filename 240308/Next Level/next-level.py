class information:
    def __init__(self,idx,lv):
        self.idx=idx
        self.lv=lv

normal=information('codetree',10)
print("user",normal.idx,"lv",normal.lv)

n,m=input().split()
user=information(n,m)
print("user",user.idx,"lv",user.lv)