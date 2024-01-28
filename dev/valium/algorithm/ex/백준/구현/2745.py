'''
https://www.acmicpc.net/problem/2745
'''

a = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14 ,'f':15, 'g':16, 'h':17, 'i':18, 'j':19, 'k':20, 'l':21, 'm':22, 'n':23, 'o':24, 'p':25, 'q':26, 'r':27, 's':28, 't':29, 'u':30, 'v':31, 'w':32, 'x':33, 'y':34, 'z':35}

def to_num(c):
  global a

  if(c in a):
    return a[c]
  else:
    return int(c)
  
if __name__ == '__main__':
  num, mal = input().split()
  mal = int(mal)
  
  out = 0
  for i, c in enumerate([*num]):
    out += to_num(c.lower()) * (mal ** (len(num) - 1 - i))

  print(out)
