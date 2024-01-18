'''
https://www.acmicpc.net/problem/1715
'''

import sys, heapq

if __name__ == '__main__':
  num = int(sys.stdin.readline())
  cards = [int(sys.stdin.readline()) for _ in range(num)]
  
  heapq.heapify(cards)
  out = 0
  while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    out = out + a + b
    heapq.heappush(cards, a + b)

  print(out)



