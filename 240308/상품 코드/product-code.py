class product:
    def __init__ (self,name,code):
        product.name=name
        product.code=code

normal=product("codetree",50)
print("product",normal.code,"is",normal.name)

n,m=input().split()
special=product(n,m)
print("product",special.code,"is",special.name)