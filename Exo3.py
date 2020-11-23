# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:06:06 2020
TP1
@author: gtchi
"""
def multiplication(A,B):
    """multiplication de matrice"""
    try:
        if len(A)!=len(B[0]):
            raise Exception("Les matrices ne peuvent pas etre multiplié")
        C=[[0 for i in range(len(A[0]))] for i in range(len(B))]
        for i in range(len(C)):
            for j in range(len(C[0])):
                for k in range(len(B)):
                    C[i][j]+=A[i][k]*B[k][j]
        return C
    except Exception as error:
        print(error)
        return 'Error'

def printMatrix(A):
    for (i,ligne) in enumerate(A):
        for (i,coeff) in enumerate(ligne):
            print(coeff,end=' ')
        print('\n')
        

A=[[1,0,1],
   [0,1,0],
   [1,0,1]]

B=[[5,6,8],
   [6,9,6],
   [3,7,6]]
print(multiplication(A,B))
printMatrix(multiplication(A,B))