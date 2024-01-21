'''
https://www.acmicpc.net/problem/17626
- 시간초과 -
'''

import math, itertools

if __name__ == '__main__':
  n = int(input())

  range = [(i + 1) * (i + 1) for i in range(math.floor(math.sqrt(n)))]
  reversed_range = sorted(range, reverse = True)
  
  is_fin = False
  for i, _ in enumerate(reversed_range):
    cur_combinations = itertools.combinations(reversed_range, i + 1)
    
    for combination in cur_combinations:

      if(sum(combination) == n):
        print(i + 1)
        is_fin = True
        break

    if(is_fin):
      break
