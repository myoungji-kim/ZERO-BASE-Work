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

