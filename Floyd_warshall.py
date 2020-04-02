"""
Floyd Warshall Algorithm

Problem Description
Given a matrix of integers A of size N x N, 
where A[i][j] represents the weight of directed edge from i to j (i ---> j).
If i==j, A[i][j]=0, and if there is no directed edge from vertex i to vertex j, A[i][j]=-1.
Return a matrix B of size N x N where B[i][j] = shortest path from vertex i to vertex j.
If there is no possible path from vertex i to vertex j , B[i][j] = -1 
Note: Rows are numbered from top to bottom and columns are numbered from left to right.
 """
#A = [ [0 , 50 , 39],[-1 , 0 , 1], [-1 , 10 , 0] ]

for k in range(len(A)):
    for i in range(len(A)):
        for j in range(len(A)):
            other_path=A[i][k]+A[k][j] if (A[i][k]>=0 and A[k][j]>=0)  else -1
            if A[i][j]==-1 :
                A[i][j]= other_path
            elif other_path==-1:
                pass
            else:
                A[i][j]=min(A[i][j],other_path)
#print(A)