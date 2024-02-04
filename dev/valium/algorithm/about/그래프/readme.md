# Graph
아래는 그래프 탐색을 위해 기초가되는 내용이므로 숙지해야한다.

## 인접 행렬 방식 구현
노드와 노드 사이의 간선 가중치를 값으로 가지는 행렬로 구성된 그래프.

![.data/img.png](img.png)
> 예제는 방향이 고려됐지만, 무지향성인 경우 대칭행렬이 된다.     
> 가중치가 고려되지 않는경우, 연결됨: 1, 끊김: 0 으로 표현하면 된다.     
> 인접 리스트 방식에 비해 메모리를 더 먹는 대신 전체탐색 속도가 빠르다.

```python
I = 123456789

graph = [
    [0, 1, I, 1, 5],
    [9, 0, 3, 2, I],
    [I, I, 0, 4, I],
    [I, I, 2, 0, 3],
    [3, I, I, I, 0]
]
```

## 탐색
파이썬에서 스택은 별도의 import 없이 사용가능하다.
```python
stack = []

stack.append(5)
stack.pop()
```  

## 인접 리스트 방식 구현
노드와 연결 된 (노드, 가중치)를 튜플로 가지는 리스트 방식의 그래프.

![.data/img_1.png](img_1.png)
> 인접 행렬 방식에 비해 메모리를 덜 먹는 대신 전체탐색 속도가 느리다.

```python
# 편의상 0번 index는 사용하지 않음
graph = [[] for _ in range(4 + 1)]

# 각 노드에 연결된 정보 (노드, 가중치)
graph[1].append((2, 1))
graph[1].append((3, 1))
graph[1].append((4, 1))

graph[2].append((3, 1))

graph[4].append((3, 1))
```

## 탐색
파이썬에서 큐는 deque 라이브러리를 사용한다.
```python
from collections import deque

queue = deque()

queue.append(5)
queue.append(6)
queue.popleft()
queue.reverse()
```
