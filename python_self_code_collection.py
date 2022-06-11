# 입출력
from sys import stdin
a = stdin.readline();



# 시간 측정
import time
startTime = time.time()
endTime = time.time()
print(startTime - endTime)



# 특정 키 값을 기준으로 정렬하기
array = [('명지', 10), ('띵지', 20), ('김띵지', 30)] 

def my_key(x):
  return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x:x[1]))


# 리스트 길이 순으로 정렬하기
words = ['aaaa', 'aaa', 'aa', 'a', 'b', 'bb', 'bbb']
words.sort(key=lambda x: len(x))



# 순열
from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result) #[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]



# 조합
from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 2))
print(result) # [('A', 'B'), ('A', 'C'), ('B', 'C')]



# 중복 순열
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result) 



# 중복 조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)



# Counter
## 리스트에 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 카운트
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력 -> 3
print(counter['green']) # 'green'가 등장한 횟수 출력 -> 1
print(dict(counter)) # 사전 자료형으로 반환 -> {'red': 2, 'blue': 3, 'green': 1}


# 최대 공약수
import math

## 최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
  return a * b // math.gcd(a, b)

a, b = 21, 14

print(math.gcd(21, 14)) # 최대 공약수 (GCD) 계산 -> 7
print(lcm(21, 14)) # 최소 공배수 (LCM) 계산 -> 42



# 유클리드 호제법 (최대공약수 계산)
def gcd(a, b):
  if a % b == 0:
    return b
  else:
    return gcd(b, a % b)

print(gcd(192, 162))



# 방향 벡터 (간단ver)
n = 5
x, y = 1, 1
plans = ['R', 'R', 'R', 'U', 'D', 'D']

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

## 이동 계획 확인
for plans in plans:
    ## 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plans == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    ## 공간 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny



# 리스트 join
alpha = ['a', 'b', 'c'] 
print(''.join(alpha)) ## abc



# isalpha
## 문자로 구성되어 있는지 확인 (숫자, 공백 안 됨)
ex1 = 'A'
print(ex1.isalpha()) ## true



# isdigit
## 숫자인지 확인
ex1 = '123456'
print(ex1.isdigit()) ## true


# isalnum
## 알파벳 또는 숫자인지 확인
ex1 = 'Hello3'
print(ex.isalnum()) ## true



# 문자열 나누기 (split)
Example_String = "Hello This is ddingji"
Split_Str = Example_String.split()
print(Split_Str) ## ['Hello', 'This', 'is', 'ddingji']

# split 횟수 지정 (maxsplit)
Examp = "V1-V2-V3-V4"
x = Examp.split("-", 1)
print(x) ## ['V1', 'V2#V3#V4']



# 특정 키 값을 기준으로 정렬하기 (lambda)
times = [list(map(int, stdin.readline().split())) for i in range(N)]
times = sorted(times, key=lambda times: times[0])
times = sorted(times, key=lambda times: times[1])
## [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9],
##  [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]



# 문자열 계산 (eval())
S = '4+5'
print(eval(S)) ## 9



# replace (문자열 대체하기)
ex1 = '가+나+다+라'
ex1.replace('+', '') ## A를 B로 바꾼다



# 우선순위 힙큐 (heapq)
import heapq
Q = []
heapq.heappush(Q, 3)
heapq.heappush(Q, 10)
heapq.heappush(Q, 5)
heapq.heappush(Q, 2)
print(Q) # [2, 3, 5, 10]
print(Q[0]) # 2
print(Q[1]) # 3



# 최소 힙
import heapq

## 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
  h = []
  result = []
  ## 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  ## 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 9, 2, 4, 6, 8, 0])
print(result) ## [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 최대 힙
import heapq

## 내림차순 힙 정렬(Heap Sort)
def heapsort(iterable):
  h = []
  result = []
  ## 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, -value)
  ## 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 9, 2, 4, 6, 8, 0])
print(result) ## [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]



# 힙 연습 문제(heap)
from sys import stdin
import heapq

N = int(stdin.readline())
heap = []

for i in range(N):
    nums = list(map(int, stdin.readline().split()))

    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
    else:
        for num in nums:
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)
                
print(heap[0])






# 다익스트라 베이직
import heapq
from sys import stdin

INF = int(1e9)  # 무한, 10억

# 노트의 개수, 간선의 개수를 입력 받기
n, m = map(int, stdin.readline().split())

# 시작 노드 번호를 입력받기
start = int(stdin.readline())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INF)라고 출력
    if distance[i] == INF:
        print("INF")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])



# 플로이드 워셜 베이직 (다익스트라)
from sys import stdin

INF = int(1e9)

n, m = map(int, stdin.readline().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][b], graph[b][a] = 1, 1

x, k = map(int, stdin.readline().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)
    
    

# 플로이드 워셜 문제 2
from sys import stdin

N = int(stdin.readline())
graph = [list(map(int, stdin.readline().split())) for i in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] == 1 and graph[k][j]:
                graph[i][j] = 1

for i in graph:
    for j in i:
        print(j, end=" ")
    print()

    
    
# DFS 기초 - 음료수 얼려먹기
def dfs(x, y):
  ## 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  
  ## 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    ## 해당 노드 방문 처리
    graph[x][y] = 1
    ## 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False

## N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

## 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

## 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS 수행
    if dfs(i, j) == True:
      result += 1
               
print(result) ## 정답 출력



# BFS 기초 - 미로탈출
def bfs(x, y):
  ## 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque()
  queue.append((x, y))
  
  ## 큐가 빌 때까지 반복하기
  while queue:
    x, y = queue.popleft()
    
    ## 현재 위치에서 4가지 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      ## 미로 찾기 공간을 벗어난 경우 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
       
      ## 벽인 경우 무시
      if graph[nx][ny] == 0:
        continue
       
      ## 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
        
  return graph[n - 1][m - 1]
               
from collections import deque

## N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

## 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))
  
## 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))




# BFS - 양과 늑대 수 세기
from sys import stdin

# '.' (점)은 빈 필드
# 글자 '#'는 울타리
# 'o'는 양, 'v'는 늑대
# 양의 수 > 늑대의 수 => 살아남음

R, C = map(int, stdin.readline().split())

visit = [[0] * C for i in range(R)]
graph = [list(stdin.readline().rstrip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = []


def BFS(x, y):
    global w, s

    visit[x][y] = 1
    queue.append([x, y])

    while queue:
        x, y = queue[0][0], queue[0][1]
        del queue[0]

        if graph[x][y] == 'v':
            w += 1
        elif graph[x][y] == 'o':
            s += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != '#' and visit[nx][ny] == 0:
                queue.append([nx, ny])
                visit[nx][ny] = 1


wolf, sheep = 0, 0

for i in range(R):
    for j in range(C):
        if graph[i][j] != '#' and visit[i][j] == 0:
            w, s = 0, 0
            BFS(i, j)
            if w >= s:
                s = 0
            else:
                w = 0

            wolf += w
            sheep += s

print(sheep, wolf)



# 부분 문자열 구하기
from sys import stdin

S = stdin.readline().rstrip()
words = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        temp = S[i:j + 1]
        words.add(temp)

print(words)
print(len(words))




# DP 문제 1 - 금쪽 상담
def solution(start, end, price):
    items = [(e, s, p) for e, s, p in zip(end, start, price)]
    items.sort()

    print(items)

    dp = [0 for _ in range(max(end) + 1)]
    for e, s, p in items:
        for j in range(e, len(dp)):
            dp[j] = max(dp[s] + p, dp[j])
    
    return dp[-1]
    

start = [1, 5, 10, 6, 5]
end = [5, 6, 12, 9, 12]
price = [10, 40, 30, 20, 50]

print(solution(start, end, price))





# DP 문제 2 - 삽질
def solution(depth, n, blocks):
    N = len(blocks[0])

    dp = [[0 for _ in range(N)]
          for _ in range(2)]

    for i in range(N):
        dp[0][i] = blocks[0][i]

    for i in range(1, depth + 1):
        for j in range(N):
            if j == 0:
                dp[i % 2][j] = min(dp[(i - 1) % 2][j:j + 2]) + blocks[i][j]
            elif j == N - 1:
                dp[i % 2][j] = min(dp[(i - 1) % 2][j - 1:j + 1]) + blocks[i][j]
            else:
                dp[i % 2][j] = min(dp[(i - 1) % 2][j - 1:j + 2]) + blocks[i][j]

        print("dp:",dp)
    return dp[depth % 2][n]

depth = 3
n = 3
blocks = [[5, 6, 2, 6],
          [1, 6, 4, 9],
          [5, 6, 9, 4],
          [55, 14, 21, 14]]

print(solution(depth, n, blocks))



# DP 문제 3 - 성 침입
def solution(N, rewards):
    dp = [0 for _ in range(N-1)]
    dp[0] = rewards[0]
    dp[1] = rewards[1]
    for i in range(2, N-1):
        dp[i] = max(dp[i-1], dp[i-2] + rewards[i])
    res = dp[-1]

    print("dp1:",dp)
    
    dp = [0 for _ in range(N)]
    dp[0] = 0
    dp[1] = rewards[1]
    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2] + rewards[i])

    print("dp2:", dp)

    return max(res, dp[-1])
    

N = 6
rewards = [5, 10, 5, 7, 5, 9]
print(solution(N, rewards))


# 세 제곱의 합 공식
(N * (N + 1) // 2) ** 2


# 문자열에서 특정 문자가 들어있는 개수 세기
from sys import stdin

N = int(stdin.readline())
count = 0

for i in range(1, N + 1):
    count += str(i).count('3')+str(i).count('6')+str(i).count('9')
print(count)



# 빙글빙글 스네이크
from sys import stdin

n = int(stdin.readline())
graph = [[' '] * n for i in range(n)]
up, right, down, left = 0, n - 1, n - 1, -2  # 이동 범위
x, y = 0, 0  # 현재 위치
move = 0
goUp, goDown, goRight, goLeft = False, False, True, False


while move < n:
    # 위로
    if goUp:
        for i in range(up, down):
            graph[i][left] = '#'

        down -= 2
        goRight = True
        goUp = False

    # 아래로
    elif goDown:
        for i in range(up, down + 1):
            graph[i][right] = '#'

        up += 2
        goLeft = True
        goDown = False

    # 오른쪽으로
    elif goRight:
        for i in range(left, right + 1):
            graph[up][i] = '#'

        left += 2
        goDown = True
        goRight = False

    # 왼쪽으로
    elif goLeft:
        for i in range(left, right):
            graph[down][i] = '#'

        right -= 2
        goUp = True
        goLeft = False

    move += 1

for g in graph:
    print("".join(g))
    
    
    
# 분할 탐색
from sys import stdin

n = int(stdin.readline())
nums1 = sorted(list(map(int, stdin.readline().split())))
m = int(stdin.readline())
nums2 = list(map(int, stdin.readline().split()))

for i in range(m):
    left, right = 0, n - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums2[i] > nums1[mid]:
            left = mid
        elif nums2[i] < nums1[mid]:
            right = mid
        else:
            isIn = True
            break

    if nums2[i] in nums1[left:right + 1]:
        print(1)
    else:
        print(0)

        
        
        
 # 팰린드롬 찾기
from sys import stdin

s = stdin.readline().rstrip()
result = []


def expand1(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


def expand2(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


for i in range(len(s)):
    result.append(len(expand1(s, i, i)))
    result.append(len(expand2(s, i, i + 1)))

print(max(result))




# 약수 구하기
def getMyDivisor(n):
    divisorsList = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            if i != 1:
                divisorsList.append(i)
            if (i ** 2) != n:
                divisorsList.append(n // i)

    return sorted(divisorsList)
  
  
  
  
  
  
