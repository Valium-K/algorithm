'''
https://www.acmicpc.net/problem/1149
시간 초과
'''


import sys

out = 123456789

def solve(mat, i, j, sum):
  global out
  
  try:
    col_num = len(mat[i])
    
    for k in range(col_num):
      if(j == k):
        continue

      if(sum > out):
        return
        
      solve(mat, i + 1, k, sum + mat[i][k])
      
  except :
    if out > sum:
      out = sum
  
if __name__ == '__main__':
  n = int(sys.stdin.readline())

  mat = []
  for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))

  solve(mat, 0, -1, 0)

  print(out)
    
