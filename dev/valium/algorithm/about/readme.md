# About
보통 1초에 1억번 연산이 가능하다 알려져있고, 알고리즘에서 입력값을 기준으로 사용 가능한 알고리즘의 상한 시간 복잡도를 추측 할 수 있다.

## 입력값 N에 대하여
### N <= 10
`O(N!)`이 가능하다.

### N <= 20
`O(2^N)`이 가능하다.

### N <= 500
`O(N^3)`이 가능하다.

### N <= 10,000
`O(Nn^2)`이 가능하다.

### N <= 5,000,000
`O(NlogN)`이 가능하다.

### N <= 100,000,000
`O(N)`이 가능하다.

### N < 100,000,000
`O(logN)`이 가능하다.