'''
https://www.acmicpc.net/problem/10157
'''

up = (0, 1)
right = (1, 0)
down = (0, -1)
left = (-1, 0)

def get_changed_dir(dir):
  if dir == up:
    return right
  elif dir == right:
    return down
  elif dir == down:
    return left
  else:
    return up

def try_sit(mat, cur):
  if mat[cur[0]][cur[1]] == 1:
    raise Exception("Already occupied or no sit")

  mat[cur[0]][cur[1]] = 1

def back(cur, dir):
  cur[0] -= dir[0]
  cur[1] -= dir[1]
  
def next(cur, dir):
  cur[0] += dir[0]
  cur[1] += dir[1]
  
if __name__ == '__main__':
  c, r = map(int, input().split())
  k = int(input())

  if(c * r < k):
    print(0)

  else:
    mat = [[0 for _ in range(r)] for _ in range(c)]
    
    dir = up
    cur = [0, 0]
    
    while k > 0:
      try:
        try_sit(mat, cur)
        next(cur, dir)
        k -= 1
      except:
        back(cur, dir)
        dir = get_changed_dir(dir)
        next(cur, dir)

    back(cur, dir)
    print(cur[0] + 1, cur[1] + 1)
