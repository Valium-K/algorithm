# 다이나믹 프로그래밍
한 번 해결된 부분 문제의 정답을 메모리에 기록하여, 한 번 계산한 답은 다시 계산하지 않도록 하는 문제 해결 기법. 다이나믹 프로그래밍은 점화식을 그대로 코드로 옮겨서 구현할 수 있다.	
다이나믹 프로그래밍을 이용한 코드 작성 방법으로는 탑다운 방식과 보텀업 방식이 있다.

# 바텀-업(상향)식 프로그래밍
`반복문`을 이용하여 작은 문제부터 풀어나가 큰 문제를 해결하는 방식.   
필요한 경우 `DP 테이블(캐싱)`을 사용해 연산 속도를 증가시킨다.

## 예제
```python
def fibo(num):
    cache = [0] * (num + 1)

    cache[1] = 1
    cache[2] = 1

    for i in range(3, num + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[num]

if __name__ == '__main__':
    print(fibo(10))

```
# 탑-다운(하향)식 프로그래밍
큰 문제를 해결하기위해 작은 문제를 호출하는 `재귀적` 방식.    
필요한 경우 `메모이제이션(캐싱)`을 사용해 한번 계산한 값을 저장해둔다

## 예제
```python
def fibo(num):
    cache = [0] * (num + 1)
    return fibo_proc(num, cache)

def fibo_proc(num, cache):
    if num <= 2:
        return 1

    if cache[num] == 0: