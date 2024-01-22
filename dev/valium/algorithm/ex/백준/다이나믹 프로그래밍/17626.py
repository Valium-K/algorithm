'''
https://www.acmicpc.net/problem/17626
'''

# import math, itertools

# if __name__ == '__main__':
#   n = int(input())

#   range = [(i + 1) * (i + 1) for i in range(math.floor(math.sqrt(n)))]
#   reversed_range = sorted(range, reverse = True)
  
#   is_fin = False
#   for i, _ in enumerate(reversed_range):
#     cur_combinations = itertools.combinations(reversed_range, i + 1)
    
#     for combination in cur_combinations:

#       if(sum(combination) == n):
#         print(i + 1)
#         is_fin = True
#         break

#     if(is_fin):
#       break

# #################################################################

import sys

if __name__ == '__main__':
  n = int(sys.stdin.readline())
  
  cache = [0 for _ in range(max(2, n + 1))]
  cache[1] = 1
  
  for i in range(2, n + 1):
      target = 4
      for j in range(1, n):
          if j ** 2 > i:
              break
          target = min(target, cache[i - (j**2)])
      cache[i] = target + 1
    
  print(cache[n])
