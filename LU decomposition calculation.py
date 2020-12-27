def mult_matrix(M, N):
    Nt = [[N[j][i] for j in range(len(N))] for i in range(len(N[0]))]
    return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in Nt] for row_m in M]

def pivot_matrix(M):
    m = len(M)
    id_mat = [[float(i ==j) for i in range(m)] for j in range(m)]

    for j in range(m):
        row = max(range(j, m), key=lambda i: abs(M[i][j]))
        if j != row:
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]

    return id_mat

def lu_decomposition(A,flag):
    n = len(A)
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    if flag == 1:
       P = pivot_matrix(A)
    else:
        P = [[float(i == j) for i in range(n)] for j in range(n)]
    PA = mult_matrix(P, A)

    for j in range(n):
        L[j][j] = 1.0

        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = PA[i][j] - s1

        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (PA[i][j] - s2) / U[j][j]


    return (P, L, U)

if __name__ == "__main__":

    A = [[18,2,0,0,-18,-2,0,0,0,0,0,0],[12,2,0,0,0,0,0,0,0,0,0,0],[8,4,2,1,0,0,0,0,0,0,0,0],[27,9,3,1,0,0,0,0,0,0,0,0,],[27,6,1,0,-27,-6,-1,0,0,0,0,0],[0,0,0,0,24,2,0,0,-24,-2,0,0],[0,0,0,0,27,9,3,1,0,0,0,0],[0,0,0,0,64,16,4,1,0,0,0,0],[0,0,0,0,0,0,0,0,30,2,0,0],[0,0,0,0,0,0,0,0,64,16,4,1],[0,0,0,0,0,0,0,0,125,25,5,1],[0,0,0,0,48,8,1,0,-48,-8,-1,0]]
    P, L, U = lu_decomposition(A,0)

    print('L=',L)
    print('U=',U)
    print('LU=',mult_matrix(L, U))
    print('P=',P)
    print('PLU=',mult_matrix(P, mult_matrix(L, U)))


b =[0,0,0.5,1/3,0,0,1/3,1/4,0,1/4,1/5,0]


def forward(L,b):
    Z = []
    for i in range(len(b)):
        Z.append(b[i])
        for j in range(i):
            Z[i] = Z[i] - (L[i][j] * Z[j])
        Z[i] = Z[i] / L[i][i]
    return Z

def backward(U,z):
    x = list(range(len(z)))
    k = len(z) - 1
    x[k] = z[k] / U[k][k]

    for i in range(k-1,-1,-1):
        Sum = 0
        for j in range(i+1,k+1):
            Sum = Sum + (U[i][j] * x[j])
        x[i] = (z[i] - Sum) / U[i][i]
    return x

z = forward(L,b)
b = backward(U,z)

print(b)