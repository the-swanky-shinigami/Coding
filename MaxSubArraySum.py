def Cross_SubASum(A, L, M, H):
    Max_Left= 0
    Max_Right= 0
    Left_Sum = -1000
    sum=0
    for i in range(M,L-1,-1):
        sum=sum+A[i]
        if sum>Left_Sum:
            Left_Sum=sum
            Max_Left=i

    Right_Sum= -1000
    sum=0

    for j in range(M+1,H+1):
        sum=sum+A[j]
        if sum>Right_Sum:
            Right_Sum=sum
            Max_Right=j

    D = Left_Sum + Right_Sum 
    return (Max_Left, Max_Right, D);

def MaxSubASum(A,L,H):
    if H==L:
        return L,H,A[L];
    else:
        M=(L+H)//2

    Left_L, Left_H, Left_Sum = MaxSubASum(A,L,M)
    Right_L, Right_H, Right_Sum = MaxSubASum(A,M+1,H)
    Cross_L, Cross_R, Cross_Sum = Cross_SubASum(A,L,M,H)

    if Left_Sum > Right_Sum and Left_Sum > Cross_Sum :
        return (Left_L, Left_H, Left_Sum);
    elif Cross_Sum > Left_Sum and Cross_Sum>Right_Sum   :
        return (Cross_L, Cross_R, Cross_Sum);
    else:
        return (Right_L, Right_H, Right_Sum);
    


A= [-1,-1]
L=0
H=len(A)-1
D,B,C=MaxSubASum(A, L, H)
print( D, B, C)
