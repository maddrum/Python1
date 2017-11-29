n=int(input())
for i in range(1,10):
    if i >= n:
        break
    for j in range(1,10):
        if j>=n:
            continue
        if n%(i+j) !=0:
            continue
        for k in range(1,10):
            if k>=n:
                continue
            for m in range(1,10):
                if m >= n:
                    continue
                sum1=i+j
                if (i+j==k+m):
                    print(str(i)+str(j)+str(k)+str(m), end=" ")
