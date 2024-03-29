# 크루스칼 알고리즘
최소 비용의 신장 트리를 찾는 알고리즘으로 간선을 Weight로 정렬한 뒤 사이클이 발생하지 않는 경우에 대하여 차례대로 최소 신장 트리를 만들어가는 그리디 알고리즘.
> 신장 트리: 모든 노드를 포함하는 부분 그래프
> 최소 신장 트리: 가중치(Weight)의 합이 최소가 되는 신장 트리

![.data/img.png](./.data/img.png)

## 구현
![.data/img2.png](./.data/img2.png)

1.  그래프(weight, a, b)를 가중치 기준으로 오름차순 정렬
2.  사이클(union 알고리즘)이 아닌경우 해당(weight, a, b)를 선택 - 그리디 알고리즘

![.data/img3.png](./.data/img2.png)

## 코드
```python
def findParent(parent, x):
    # root 까지 부모를 따라 올라감
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)

    # node index가 작은 node를 부모로 선택
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def printResult(result):
    print('최소 스패닝 트리:')
    for g in sorted(result):
        print(g)
    print('최소 스패닝 트리의 가중치 합:', sum(map(lambda x: x[2], result)))

if __name__ == '__main__':
    graph = []
    node, edge = map(int, input().split())
    for _ in range(edge):
        a, b, weight = map(int, input().split())
        graph.append((weight, a, b))
    graph.sort()

    # 초기 parent는 root와 같고 그것은 자기 자신이다.
    parent = [i for i in range(node + 1)]
    result = []
    for weight, a, b in graph:
        if findParent(parent, a) != findParent(parent, b):
            unionParent(parent, a, b)
            result.append((a, b, weight))

    printResult(result)
```