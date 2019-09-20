# -*- coding: utf-8 -*-

def eliminacaoGaussiana():
    
    matrix = [
        [5,2,1,7],  
        [3,1,4,7],  
        [1,1,3,13]
    ]

    n = len(matrix)
    c = len(matrix[0])
    
    for k in range(0,n-1):
        for i in range(k+1, n):
            for j in range(k,n):
                elemento = matrix[i][j]
                print('ijk', (i,j,k))
                matrix[i][j] = elemento - matrix[k][j] * matrix[i][k]/matrix[k][k]

    print(matrix)