word=input()
n=len(word)
print(word)
new_str=word[-1]+word[:4]
for i in range(n):
    print(new_str)
    new_str=new_str[-1]+new_str[:4]