'''
https://www.acmicpc.net/problem/2577
'''

if __name__ == '__main__':
  a = int(input())
  b = int(input())
  c = int(input())

  mult_string = str(a * b * c)

  out = [0] * 10
  for i in [*mult_string]:
    out[int(i)] += 1

  for i in out:
    print(i)
