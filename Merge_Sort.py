def Merge_Sort(A,p,r):
    while p<r:
        if (r-p)%2==1:
            q=(r-p-1)/2
        else:
            q=(r-p)/2
        Merge_Sort(A,p,q)
        Merge_Sort(A,q,r)
        Merge(A,p,q,r)

def Merge(A,p,q,r):
    a1=[]
    a2=[]
    for i in range(p,q):
        a1.append(A[i])
    for j in range(q,r):
        a2.append(A[j])
