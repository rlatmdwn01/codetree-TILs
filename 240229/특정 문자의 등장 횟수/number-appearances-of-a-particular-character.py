word=input()

start_idx=-1
n=len(word)
ee_cnt=0
eb_cnt=0

for i in range(n-1):
    if word[i]=='e' and word[i+1]=='e':
        ee_cnt+=1
    elif word[i]=='e' and word[i+1]=='b':
        eb_cnt+=1

print(ee_cnt,eb_cnt)