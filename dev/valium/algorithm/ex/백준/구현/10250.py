'''
https://www.acmicpc.net/problem/10250
'''

import math

if __name__ == '__main__':
    line = input()
    out = []
    for _ in range(int(line)):
      a, c, b = map(int, input().split())

      first = a if b % a == 0 else b % a
      second = format(math.ceil(b / a), '02')

      out.append(str(first) +str(second))

    for _, v in enumerate(out):
      print(v)
