score_list=list(map(float,input().split()))

sum_val=sum(score_list)
n=len(score_list)

print("%.1f"%(sum_val/n))