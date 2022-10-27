#iterativa
def ar(m,i,j):
    return[row[:j]+row[j+1:] for row in (m[: i] + m[i+1:])]
def detrec(matriz):
    Sum=0
    for i in range(len(matriz)):
        sign = (-1) ** (i)
        sub_det = detrec(assist(mat, 0, i))
        Sum += (sign * mat[0][i] * sub_det)
    return Sum

#recursiva
def alit(B):
    n=len(B)
    Al=B
    for s in range(n):
        for i in range(s+1,n):
            if Al[s][s] == 0:
                Al[s][s]== 1.0e-18
            at =Al[i][s]/Al[s][s]
        for j in range (n):
            Al[i][j]= Al[i][j]-at*Al[s][j]
    solution = 1.0
    for i in range(n):
        solution *= Al[i][i] 
    return solution
            